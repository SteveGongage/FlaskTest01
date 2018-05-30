from flask_restful import Resource


class Hello(Resource):
    def get(self):
        print('I am a meat popsicle')
        print('test')
        
        return {"message": "Hello, World!"}