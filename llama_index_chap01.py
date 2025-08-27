# pip install llama-index
# pip install ipykernel

print("Hello")


# https://github.com/run-llama/llama_index/tree/main/llama-datasets/paul_graham_essay 

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# !llamaindex-cli download-llamadataset PaulGrahamEssayDataset --download-dir ./data

# 1. 데이터 로드

documents = SimpleDirectoryReader("data").load_data()

# 2. 인덱스 생성
index = VectorStoreIndex.from_documents(documents)

len(documents)
print(documents)

# 3. 쿼리엔진 객체 생성
query_engine = index.as_query_engine()

# 4. 질의응답 실행
response = query_engine.query("이 문서 전체를 번역해. 구절 빠짐없이 한국어로")

print(response)
type(response)
response.response
response.source_nodes # list of nodes
len(response.source_nodes)
type(response.source_nodes[1].text)
response.source_nodes[0].text


##  indexing 과정 세부적으로 살펴보기

from dotenv  import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# 2. 데이터 변환 (Node 분할)
from llama_index.core.node_parser import SentenceSplitter

# 문장을 기준으로 적당한 크기로 잘라서 노드화
splitter = SentenceSplitter(chunk_size=200, chunk_overlap=20)
nodes = splitter.get_nodes_from_documents(documents)


# 3. 인덱싱 실행
index = VectorStoreIndex(nodes)


###########  ch02 ###########
# pip install docx2txt  # docx 파일 읽기
# pip install PyPDF2    # pdf 파일 읽기
# pip install openpyxl  # xlsx 파일 읽기

from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader("sample_docs").load_data()
len(documents)
documents = SimpleDirectoryReader("sample_docs", recursive=True).load_data() # 하위 폴더까지 탐색
len(documents)
print(documents[0].text)
print(documents[0].metadata) # 메타데이터


from llama_index.core import Document

# 텍스트 데이터를 기반으로 문서 생성
document_text = "영화 '기생충'은 가난한 가족인 기우네가 부유한 박 사장네 집에 하나씩 취업하면서 벌어지는 이야기입니다. 처음에는 평화로워 보이지만, 이들의 거짓말이 쌓이며 긴장감이 점점 고조됩니다. 박 사장네 집에는 비밀 지하실이 존재하며, 그곳에는 오랫동안 숨어 살던 남자가 있다는 반전이 있습니다. 이 사실을 알게 된 기우네 가족은 예상치 못한 위기를 맞이하게 됩니다. 결국 극한 상황에서 벌어지는 사건으로 인해 비극적인 결말로 이어집니다."
document = Document(text=document_text)

# 메타데이터 추가
document.metadata = {'author': '영화 해설', 'subject': '기생충 줄거리'}

print(document)

from llama_index.core.node_parser import SimpleNodeParser

parser = SimpleNodeParser(chunk_size=80, chunk_overlap=0)
nodes = parser.get_nodes_from_documents([document])

print("\n생성된 노드들")
for idx, node in enumerate(nodes, start=1):
    node.metadata = {'type': '영화 줄거리', 'genre': '드라마', 'node_id': idx}
    print(f"노드 {idx}: {node.text}")
    print(f"메타데이터: {node.metadata}")