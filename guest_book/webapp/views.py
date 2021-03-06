from django.shortcuts import render

# Create your views here.
{

}

def home(request):
    return render(request, 'index.html')

def add_recording(request):
    if request.method == 'GET':
        return render(request, 'recording_add.html')
    elif request.method == 'POST':
        content = [
            {
                'author': 'Vasya Pupkin',
                'email': 'vasyapupkin@example.com',
                'content': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit nam eius officiis molestias? Quo quos facilis maiores numquam ex consequuntur fuga modi quis natus sit? Non eius repellendus similique repudiandae?',
                'created_at': 15,
                'udated_at': 15,
                'status': 'active'
            },

            {
                'author': 'John Doe',
                'email': 'johndoe@example.com',
                'content': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit nam eius officiis molestias? Quo quos facilis maiores numquam ex consequuntur fuga modi quis natus sit? Non eius repellendus similique repudiandae?',
                'created_at': 15,
                'udated_at': 15,
                'status': 'active'
            },

            {
                'author': 'Lisa',
                'email': 'lisa@example.com',
                'content': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit nam eius officiis molestias? Quo quos facilis maiores numquam ex consequuntur fuga modi quis natus sit? Non eius repellendus similique repudiandae?',
                'created_at': 15,
                'udated_at': 15,
                'status': 'active'
            },

            {
                'author': 'Bob',
                'email': 'bob@example.com',
                'content': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit nam eius officiis molestias? Quo quos facilis maiores numquam ex consequuntur fuga modi quis natus sit? Non eius repellendus similique repudiandae?',
                'created_at': 15,
                'udated_at': 15,
                'status': 'blocked'
            },

            {
                'author': 'Ben',
                'email': 'ben@example.com',
                'content': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit nam eius officiis molestias? Quo quos facilis maiores numquam ex consequuntur fuga modi quis natus sit? Non eius repellendus similique repudiandae?',
                'created_at': 15,
                'udated_at': 15,
                'status': 'active'
            },
        ]
        return render(request, 'index.html')