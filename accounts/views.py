from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # 폼 객체에 지정된 모델을 확인하고 이 모델의 객체를 생성
            new_user.set_password(user_form.cleaned_data['password']) # 암호화된 비밀번호를 지정
            new_user.save() # 실제로 DB에 저장
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'form': user_form})

