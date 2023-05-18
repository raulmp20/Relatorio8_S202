
class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, result, jogador_nome):
        query = "MATCH (j:Jogador {name: $jogador_nome}) CREATE (:Partida {result: $result})<-[:PARTICIPA]-(j)"
        parameters = {"result": result, "jogador_nome": jogador_nome}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (p:Partida)<-[:PARTICIPOU]-(j1:Jogador) RETURN p.result AS result, j1.name AS jogador1_name"
        results = self.db.execute_query(query)
        return [(result["result"], result["jogador1_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (j:Jogador {name: $old_name}) SET j.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_jogador_partida(self, jogador_name, partida_result):
        query = "MATCH (j:Jogador {name: $jogador_name}) MATCH (p:Partida {result: $partida_result}) CREATE (j)-[:PARTICIPA]->(p)"
        parameters = {"jogador_name": jogador_name, "partida_result": partida_result}
        self.db.execute_query(query, parameters)


    def delete_jogador(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_partida(self, result):
        query = "MATCH (p:Partida {result: $result})<-[:PARTICIPOU]-(j:Jogador) DETACH DELETE p"
        parameters = {"result": result}
        self.db.execute_query(query, parameters)