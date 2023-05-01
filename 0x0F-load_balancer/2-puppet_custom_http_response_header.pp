# Puppet script to create a custom HTTP header response

exec { 'add_header':
	provider => shell,
	command  => 'sudo apt-get -y update && sudo apt-get install -y nginx && mkdir -p /var/www/html && echo "Hello World!" | sudo tee /var/www/html/index.html && string_for_replacement="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.https://www.youtube.com/watch?v=MAjD6iaMqXU permanent;" && sudo sed -i "s/server_name _;/$string_for_replacement/" /etc/nginx/sites-enabled/default && echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html && string_for_replacement="listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}" && sudo sed -i "s/listen 80 default_server;/$string_for_replacement/" /etc/nginx/sites-enabled/default && sudo sed -i '/^\slocation.*/i \        add_header X-Served-By $hostname;' /etc/nginx/sites-enabled/default && sudo service nginx restart',
}
