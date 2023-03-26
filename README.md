# DesafioFullStackBack

<h1>Contact ME</h1>

<h3><strong>Proposta:</strong></h3>
<p>........</p>
<hr noshade />

<h2>Acesso a documentação: </h2>
<h3>api/docs/swagger-ui/</h3>

<h2>[201] Criar usuário </h2>
<h3>POST - api/user/</h3>

<strong>Essa rota não necessita autenticação. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string, máximo 150 chars e apenas letras, números e @/./+/-/_</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 128 chars.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email e máximo 127 chars.</li>
    <li><strong>phone: </strong>Entrada obrigatória do tipo string e máximo 11 chars.</li>
    <li><strong>first_name: </strong>Entrada obrigatória do tipo string e máximo 127 chars.</li>
    <li><strong>last_name: </strong>Entrada obrigatória do tipo string e máximo 127 chars.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
	"id": "30c5acf5-eb86-4a1e-b845-3b86eb177627",
	"username": "Test@User",
	"email": "test@mail.com",
	"name": "Test User",
	"phone": "00123456789",
	"registered_at": "2023-03-26",
	"contacts": []
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto/vazio:</p>
<pre>
{
	"username": [
		"This field is required."
	],
	"email": [
		"This field is required."
	],
	"first_name": [
		"This field is required."
	],
	"last_name": [
		"This field is required."
	],
	"phone": [
		"This field is required."
	],
	"password": [
		"This field is required."
	]
}
</pre>

<h2>[200] Lista o próprio usuário.</h2>
<h3> GET -api/user/</h3>

<strong>Essa rota necessita autenticação:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem bem sucedida:</p>
<pre>
[
	{
		"id": "30c5acf5-eb86-4a1e-b845-3b86eb177627",
		"username": "Test@User",
		"email": "test@mail.com",
		"name": "Test User",
		"phone": "00123456789",
		"registered_at": "2023-03-26",
		"contacts": [
			{
				"id": "2881825f-d0ea-4953-8f68-5bfb9a7d32ed",
				"email": "test1@mail.com",
				"name": "Test User",
				"phone": "123456789",
				"registered_at": "2023-03-26"
			}
		]
	}
]
</pre>
<hr noshade />

<h2>[200] Atualizar usuário:</h2>
<h3>PATCH - api/user/:user_id/</h3>

<strong>Essa rota necessita autenticação, é preciso enviar o id do usuário como parâmetro e apenas o próprio usuário pode realizar:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para atualização realizada com sucesso:</p>
<pre>
{
	"id": "30c5acf5-eb86-4a1e-b845-3b86eb177627",
	"username": "Test@User",
	"email": "test@mail.com",
	"name": "Test User",
	"phone": "00123456789",
	"registered_at": "2023-03-26",
	"contacts": [
		{
			"id": "2881825f-d0ea-4953-8f68-5bfb9a7d32ed",
			"email": "test1@mail.com",
			"name": "Test User",
			"phone": "123456789",
			"registered_at": "2023-03-26"
		}
	]
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para usuário inexistente ou não encontrado:</p>
<pre>
{
	"detail": "Not found."
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para caso não seja o próprio usuário:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>
<hr noshade />

<h2>[201] Criar contato </h2>
<h3>POST - api/contact/</h3>

<strong>Essa rota necessita autenticação. Campos de envio para request:</strong>

<ul>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email e máximo 127 chars.</li>
    <li><strong>phone: </strong>Entrada obrigatória do tipo string e máximo 11 chars.</li>
    <li><strong>first_name: </strong>Entrada obrigatória do tipo string e máximo 127 chars.</li>
    <li><strong>last_name: </strong>Entrada obrigatória do tipo string e máximo 127 chars.</li>
</ul>



<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
	"id": "2881825f-d0ea-4953-8f68-5bfb9a7d32ed",
	"email": "test@mail.com",
	"name": "Test User",
	"phone": "00123456789",
	"registered_at": "2023-03-26"
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto/vazio:</p>
<pre>
{
	"email": [
		"This field is required."
	],
	"first_name": [
		"This field is required."
	],
	"last_name": [
		"This field is required."
	],
	"phone": [
		"This field is required."
	]
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação por token:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>
<hr noshade />

<h2>[200] Listar contatos do usuário.</h2>
<h3> GET -api/contact/</h3>

<strong>Essa rota necessita autenticação:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem bem sucedida:</p>
<pre>
[
	{
		"id": "c36fa7bb-e695-4ca5-bb84-a8d56cba135b",
		"email": "test1@mail.com",
		"name": "Test User",
		"phone": "123456789",
		"registered_at": "2023-03-26"
	},
	{
		"id": "370bd6cf-3798-43c0-a792-2392f5876efe",
		"email": "test2@mail.com",
		"name": "Test User",
		"phone": "123456789",
		"registered_at": "2023-03-26"
	}
]
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>
<hr noshade />

<h2>[200] Listar um contato específico:</h2>
<h3>GET - api/contact/:contact_id/</h3>

<strong>Essa rota necessita de autenticação, é preciso enviar o id do contato como parâmetro e o usuário deve ser o dono do contato:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para retorno bem sucedido:</p>
<pre>
{
    "id": "c36fa7bb-e695-4ca5-bb84-a8d56cba135b",
    "email": "test1@mail.com",
    "name": "Test User",
    "phone": "123456789",
   "registered_at": "2023-03-26"
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para contato inexistente ou não encontrado:</p>
<pre>
{
    "detail": "Not found."
}
</pre>
<hr noshade />

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para contato que não pertença ao usuário:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>
<hr noshade />

<h2>[200] Atualizar um contato específico</h2>
<h3>PATCH - api/contact/:contact_id/</h3>

<strong>Essa rota necessita de autenticação, é preciso enviar o id do contato como parâmetro e o usuário deve ser o dono do contato:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para atualização realizada com sucesso:</p>
<pre>
{
	"id": "c36fa7bb-e695-4ca5-bb84-a8d56cba135b",
	"email": "test2@mail.com",
	"name": "Test User",
	"phone": "123456789",
	"registered_at": "2023-03-26"
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para contato inexistente ou não encontrado:</p>
<pre>
{
    "detail": "Not found."
}
</pre>
<hr noshade />

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para contato que não pertença ao usuário:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>
<hr noshade />