import numpy as np

def cal_cos_sim(doc,query):
    cos_sim = np.dot(doc,query)/(np.linalg.norm(doc) * np.linalg.norm(query))
    return cos_sim

def main():
    Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query = np.array([1,1,0,0,1,0])
    doc1 = cal_cos_sim(Docs[0],Query)
    doc2 = cal_cos_sim(Docs[1],Query)
    doc3 = cal_cos_sim(Docs[2],Query)

    print(f"doc1={doc1:0.2f}")
    print(f"doc2={doc2:0.2f}")
    print(f"doc2={doc3:0.2f}")

if __name__=='__main__':
    main()
