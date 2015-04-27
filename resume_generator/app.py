from flask import Flask
from flask.ext.restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Resume Generator API',
    description='An API used to integrate resume information from various formats and transform them into different graphical representations.')

ns = api.namespace('resumes', description='Resumes')

resume_parser = api.parser()
resume_parser.add_argument('username', type=str, required=True, help='Your username, used as an identifier for any request to the API', location='form')
resume_parser.add_argument('fullname', type=str, required=True, help='Your full name', location='form')
resume_parser.add_argument('age',      type=int, required=True, help='Your age', location='form')

resume = api.model('Resume', {
  'username': fields.String(required=True),
  'fullname': fields.String(required=True),
  'age'     : fields.Integer(required=True)
})

SUPPORTED_INPUTS = ['json']

resume_content_parser = api.parser()
resume_content_parser.add_argument('content',      type=str, required=True, help='The resume content in the format described by content_type.', location='form')
resume_content_parser.add_argument('content_type', type=str, required=True, help='The resume content type submitted. Currently supported: ' + ', '.join(SUPPORTED_INPUTS), location='form')

resume_content = api.model('ResumeContent', {
  'content'        : fields.String(required=True),
  'content_type'   : fields.String(required=True, enum=SUPPORTED_INPUTS),
})

SUPPORTED_VIEWS = ['kibana3']

resume_view_parser = api.parser()
resume_view_parser.add_argument('view',         type=str, required=True, help='The visual representation desired. Currently supported: ' + ', '.join(SUPPORTED_VIEWS), location='form')
resume_view_parser.add_argument('other_params', type=str, required=False, help='Other parameters depending on the view selected.', location='form')

resume_view = api.model('ResumeView', {
  'view'         : fields.String(required=True, enum=SUPPORTED_VIEWS),
  'other_params' : fields.Arbitrary(required=False)
})

@ns.route('/')
class Resume(Resource):

  @api.doc(parser=resume_parser)
  @api.marshal_with(resume, code=201)
  def post(self):
    return True

@ns.route('/<string:username>/content')
@api.doc(responses={201: 'Created', 404: 'Resume not found'}, params={'username': 'Your username'})
class ResumeContent(Resource):

  @api.doc(parser=resume_content_parser)
  @api.marshal_with(resume_content)
  def post(self, username):
    args = parser.parse_args()
    content = {'content': args['content']}
    content_type = {'content_type': args['content_type']}
    return True

@ns.route('/<string:username>/view')
@api.doc(responses={200: 'OK', 404: 'Resume not found'}, params={'username': 'Your username'})
class ResumeView(Resource):

  @api.doc(parser=resume_view_parser)
  @api.marshal_with(resume_view)
  def put(self, username):
    args = parser.parse_args()
    view = {'view': args['view']}
    return 'public link to this view'

if __name__ == '__main__':
    app.run(debug=True)

