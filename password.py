password = 'a123456'
i = 3
while i > 0:	
	key = input('請輸入密碼：')
	if key == password:
		print('登入成功!')
		break
	else:
		i =  i - 1 
		print('密碼錯誤!你還有', i ,'次機會')

