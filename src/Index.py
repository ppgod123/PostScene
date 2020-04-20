from post_scene.post_scene import PostScene

xmind_path = './yaml/demo.yaml'  # 脚本文件的路径
api_document_path = './api_document/demo.postman_collection.json'  # postman json data 文件的路径


PostScene.covert(xmind_path, api_document_path,scene_dirs='./scene')

