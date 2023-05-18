from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://52.90.178.103:7687", "neo4j", "laundry-commas-apple")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Raul")
game_db.create_player("Cris")
game_db.create_player("Paulo")
game_db.create_player("Bruno")

# Criando algumas partidas e suas relações com os jogadores
game_db.create_match("2x1", "Raul")
game_db.create_match("7x3", "Paulo")
game_db.create_match("7x4", "Bruno")
game_db.create_match("4x2", "Cris")

# Atualizando o nome de um jogador
game_db.update_player("Paulo", "Joao")

game_db.insert_jogador_partida("Joao", "4x2")
game_db.insert_jogador_partida("Cris", "2x1")
game_db.insert_jogador_partida("Raul", "7x3")


# Deletando um jogador e uma partida
game_db.delete_jogador("Cris")
game_db.delete_partida("7x3")

# Print de todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Partidas:")
print(game_db.get_match())

# Fechando a conexão
db.close()