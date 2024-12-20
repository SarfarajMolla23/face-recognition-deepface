import json

from deepface import DeepFace

# face mathcing
# result = DeepFace.verify(img1_path="sarfaraj_1.jpg",
                        # img2_path="not_sarfaraj_2.jpg")
# print(json.dumps(result, indent=2))

# find face in db
# dfs = DeepFace.find(
   # img_path="sarfaraj_2.jpg", db_path="./db")
# print(dfs)

# face analysis
objs = DeepFace.analyze(
  img_path = "sarfaraj_2.jpg",
  actions = ['age', 'gender', 'race', 'emotion'],
)
print(json.dumps(objs, indent=2))

