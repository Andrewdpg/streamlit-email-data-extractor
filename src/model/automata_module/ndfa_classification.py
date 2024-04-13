import copy

import pandas as pd
from pyformlang.finite_automaton import (NondeterministicFiniteAutomaton,
                                         State, Symbol)


# Non-deterministic Finite Automaton
class SpamClassification:
    
    def __init__(self, default_nfa, s, f): 
        self.offer = copy.deepcopy(default_nfa)

        self.offer.add_transitions([
            (s, 'o', 's1'), (s, 'O', 's1'),
            ('s1', 'f', 's2'), ('s1', 'F', 's2'),
            ('s2', 'e', 's3'), ('s2', 'E', 's3'),
            ('s3', 'r', 's4'), ('s3', 'R', 's4'),
            ('s4', 't', 's5'), ('s4', 'T', 's5'),
            ('s5', 'a', f), ('s5', 'A', f)
        ])

        self.subscribe = copy.deepcopy(default_nfa)

        self.subscribe.add_transitions([
            (s, 's', 's1'), (s, 'S', 's1'),
            ('s1', 'u', 's2'), ('s1', 'U', 's2'),
            ('s2', 's', 's3'), ('s2', 'S', 's3'),
            ('s3', 'c', 's4'), ('s3', 'C', 's4'),
            ('s4', 'r', 's5'), ('s4', 'R', 's5'),
            ('s5', 'i', 's6'), ('s5', 'I', 's6'),
            ('s6', 'p', 's7'), ('s6', 'P', 's7'),
            ('s7', 'c', 's8'), ('s7', 'C', 's8'),
            ('s8', 'i', 's9'), ('s8', 'I', 's9'),
            ('s9', 'ó', 's10'), ('s9', 'O', 's10'),
            ('s10', 'n', f), ('s10', 'N', f)
        ])

        self.discount = copy.deepcopy(default_nfa)

        self.discount.add_transitions([
            (s, 'd', 's1'), (s, 'D', 's1'),
            ('s1', 'e', 's2'), ('s1', 'E', 's2'), 
            ('s2', 's', 's3'), ('s2', 'S', 's3'),
            ('s3', 'c', 's4'), ('s3', 'C', 's4'),
            ('s4', 'u', 's5'), ('s4', 'U', 's5'),
            ('s5', 'e', 's6'), ('s5', 'E', 's6'),
            ('s6', 'n', 's7'), ('s6', 'N', 's7'),
            ('s7', 't', 's8'), ('s7', 'T', 's8'),
            ('s8', 'o', f), ('s8', 'O', f)
        ])

        self.opportunity = copy.deepcopy(default_nfa)

        self.opportunity.add_transitions([
            (s, 'o', 's1'), (s, 'O', 's1'),
            ('s1', 'p', 's2'), ('s1', 'P', 's2'),
            ('s2', 'o', 's3'), ('s2', 'O', 's3'),
            ('s3', 'r', 's4'), ('s3', 'R', 's4'),
            ('s4', 't', 's5'), ('s4', 'T', 's5'),
            ('s5', 'u', 's6'), ('s5', 'U', 's6'),
            ('s9', 'a', 's10'), ('s9', 'A', 's10'),
            ('s6', 'n', 's7'), ('s6', 'N', 's7'),
            ('s7', 'i', 's8'), ('s7', 'I', 's8'),
            ('s8', 'd', 's9'), ('s8', 'D', 's9'),
            ('s10', 'd', f), ('s10', 'D', f)
        ])

        self.special_price = copy.deepcopy(default_nfa)

        self.special_price.add_transitions([
            (s, 'p', 's1'), (s, 'P', 's1'),
            ('s1', 'r', 's2'), ('s1', 'R', 's2'),
            ('s2', 'e', 's3'), ('s2', 'E', 's3'),
            ('s3', 'c', 's4'), ('s3', 'C', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'o', 's6'), ('s5', 'O', 's6'),
            ('s6', ' ', 's7'), ('s6', ' ', 's7'),
            ('s7', 'e', 's8'), ('s7', 'E', 's8'),
            ('s8', 's', 's9'), ('s8', 'S', 's9'),
            ('s9', 'p', 's10'), ('s9', 'P', 's10'),
            ('s10', 'e', 's11'), ('s10', 'E', 's11'),
            ('s11', 'c', 's12'), ('s11', 'C', 's12'),
            ('s12', 'i', 's13'), ('s12', 'I', 's13'),
            ('s13', 'a', 's14'), ('s13', 'A', 's14'),
            ('s14', 'l', f), ('s14', 'L', f)
        ])

    # oferta
    # oferton
    def __spam_offer(self, text):
        count = 0

        if (self.offer.accepts(text)):
            count += 1

        return count

       
    # suscripción
    # suscribirse
    def __spam_subscribe(self, text):
        count = 0

        if (self.subscribe.accepts(text)):
            count += 1
        
        return count

    # descuento
    # rebaja
    def __spam_discount(self, text):
        count = 0

        if (self.discount.accepts(text)):
            count += 1

        return count


    # oportunidad
    def __spam_opportunity(self, text):
        count = 0

        if (self.opportunity.accepts(text)):
            count += 1

        return count

    # precio especial
    def __spam_special_price(self, text):
        count = 0

        if (self.special_price.accepts(text)):
            count += 1
        
        return count

    def execute(self, text):
        score = 0
        score += self.__spam_offer(text)
        score += self.__spam_subscribe(text)
        score += self.__spam_discount(text)
        score += self.__spam_opportunity(text)
        score += self.__spam_special_price(text)

        return score

class InvitationClassification:
    
    def __init__(self, default_nfa, s, f):
        # Confirmación
        self.confirmation = copy.deepcopy(default_nfa)

        self.confirmation.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'o', 's2'), ('s1', 'O', 's2'),
            ('s2', 'n', 's3'), ('s2', 'N', 's3'),
            ('s3', 'f', 's4'), ('s3', 'F', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'r', 's6'), ('s5', 'R', 's6'),
            ('s6', 'm', 's7'), ('s6', 'M', 's7'),
            ('s7', 'a', 's8'), ('s7', 'A', 's8'),
            ('s8', 'c', 's9'), ('s8', 'C', 's9'),
            ('s9', 'i', 's10'), ('s9', 'I', 's10'),
            ('s10', 'ó', 's11'), ('s10', 'Ó', 's11'),
            ('s11', 'n', f), ('s11', 'N', f)
        ])

        # Confirmar
        self.confirm = copy.deepcopy(default_nfa)

        self.confirm.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'o', 's2'), ('s1', 'O', 's2'),
            ('s2', 'n', 's3'), ('s2', 'N', 's3'),
            ('s3', 'f', 's4'), ('s3', 'F', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'r', 's6'), ('s5', 'R', 's6'),
            ('s6', 'm', 's7'), ('s6', 'M', 's7'),
            ('s7', 'a', 's8'), ('s7', 'A', 's8'),
            ('s8', 'r', f), ('s8', 'R', f)
        ])
        
        # Convocatoria
        self.call = copy.deepcopy(default_nfa)

        self.call.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'o', 's2'), ('s1', 'O', 's2'),
            ('s2', 'n', 's3'), ('s2', 'N', 's3'),
            ('s3', 'v', 's4'), ('s3', 'V', 's4'),
            ('s4', 'o', 's5'), ('s4', 'O', 's5'),
            ('s5', 'c', 's6'), ('s5', 'C', 's6'),
            ('s6', 'a', 's7'), ('s6', 'A', 's7'),
            ('s7', 't', 's8'), ('s7', 'T', 's8'),
            ('s8', 'o', 's9'), ('s8', 'O', 's9'),
            ('s9', 'r', 's10'), ('s9', 'R', 's10'),
            ('s10', 'i', 's11'), ('s10', 'I', 's11'),
            ('s11', 'a', f), ('s11', 'A', f)
        ])

        # Participar
        self.participate = copy.deepcopy(default_nfa)

        self.participate.add_transitions([
            (s, 'p', 's1'), (s, 'P', 's1'),
            ('s1', 'a', 's2'), ('s1', 'A', 's2'),
            ('s2', 'r', 's3'), ('s2', 'R', 's3'),
            ('s3', 't', 's4'), ('s3', 'T', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'c', 's6'), ('s5', 'C', 's6'),
            ('s6', 'i', 's7'), ('s6', 'I', 's7'),
            ('s7', 'p', 's8'), ('s7', 'P', 's8'),
            ('s8', 'a', 's9'), ('s8', 'A', 's9'),
            ('s9', 'r', f), ('s9', 'R', f)
        ])

        # Asistir
        self.assist = copy.deepcopy(default_nfa)

        self.assist.add_transitions([
            (s, 'a', 's1'), (s, 'A', 's1'),
            ('s1', 's', 's2'), ('s1', 'S', 's2'),
            ('s2', 'i', 's3'), ('s2', 'I', 's3'),
            ('s3', 's', 's4'), ('s3', 'S', 's4'),
            ('s4', 't', 's5'), ('s4', 'T', 's5'),
            ('s5', 'i', 's6'), ('s5', 'I', 's6'),
            ('s6', 'r', f), ('s6', 'R', f)
        ])

    def __invitation_confirmation(self, text):
        count = 0

        if (self.confirmation.accepts(text)):
            count += 1

        return count
    
    def __invitation_confirm(self, text):
        count = 0

        if (self.confirm.accepts(text)):
            count += 1

        return count
    
    def __invitation_call(self, text):
        count = 0

        if (self.call.accepts(text)):
            count += 1

        return count
    

    def __invitation_participate(self, text):
        count = 0

        if (self.participate.accepts(text)):
            count += 1

        return count
    
    def __invitation_assist(self, text):
        count = 0

        if (self.assist.accepts(text)):
            count += 1

        return count
    
    def execute(self, text):
        score = 0
        score += self.__invitation_confirmation(text)
        score += self.__invitation_confirm(text)
        score += self.__invitation_call(text)
        score += self.__invitation_participate(text)
        score += self.__invitation_assist(text)

        return score

class SecurityClassification:

    def __init__(self, default_nfa, s, f):
        # Clave de acceso
        self.access_key = copy.deepcopy(default_nfa)

        self.access_key.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'l', 's2'), ('s1', 'L', 's2'),
            ('s2', 'a', 's3'), ('s2', 'A', 's3'),
            ('s3', 'v', 's4'), ('s3', 'V', 's4'),
            ('s4', 'e', 's5'), ('s4', 'E', 's5'),
            ('s5', ' ', 's6'), ('s5', ' ', 's6'),
            ('s6', 'd', 's7'), ('s6', 'D', 's7'),
            ('s7', 'e', 's8'), ('s7', 'E', 's8'),
            ('s8', ' ', 's9'), ('s8', ' ', 's9'),
            ('s9', 'a', 's10'), ('s9', 'A', 's10'),
            ('s10', 'c', 's11'), ('s10', 'C', 's11'),
            ('s11', 'c', 's12'), ('s11', 'C', 's12'),
            ('s12', 'e', 's13'), ('s12', 'E', 's13'),
            ('s13', 's', 's14'), ('s13', 'S', 's14'),
            ('s14', 'o', f), ('s14', 'O', f)
        ])

        # Código de autenticación
        self.authentication_code = copy.deepcopy(default_nfa)

        self.authentication_code.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'ó', 's2'), ('s1', 'Ó', 's2'),
            ('s2', 'd', 's3'), ('s2', 'D', 's3'),
            ('s3', 'i', 's4'), ('s3', 'I', 's4'),
            ('s4', 'g', 's5'), ('s4', 'G', 's5'),
            ('s5', 'o', 's6'), ('s5', 'O', 's6'),
            ('s6', ' ', 's7'), ('s6', ' ', 's7'),
            ('s7', 'd', 's8'), ('s7', 'D', 's8'),
            ('s8', 'e', 's9'), ('s8', 'E', 's9'),
            ('s9', ' ', 's10'), ('s9', ' ', 's10'),
            ('s10', 'a', 's11'), ('s10', 'A', 's11'),
            ('s11', 'u', 's12'), ('s11', 'U', 's12'),
            ('s12', 't', 's13'), ('s12', 'T', 's13'),
            ('s13', 'e', 's14'), ('s13', 'E', 's14'),
            ('s14', 'n', 's15'), ('s14', 'N', 's15'),
            ('s15', 't', 's16'), ('s15', 'T', 's16'),
            ('s16', 'i', 's17'), ('s16', 'I', 's17'),
            ('s17', 'c', 's18'), ('s17', 'C', 's18'),
            ('s18', 'a', 's19'), ('s18', 'A', 's19'),
            ('s19', 'c', 's20'), ('s19', 'C', 's20'),
            ('s20', 'i', 's21'), ('s20', 'I', 's21'),
            ('s21', 'ó', 's22'), ('s21', 'Ó', 's22'),
            ('s22', 'n', f), ('s22', 'N', f)
        ])

        # Nuevo inicio de inicio sesión
        self.login_verification = copy.deepcopy(default_nfa)

        self.login_verification.add_transitions([
            (s, 'n', 's1'), (s, 'N', 's1'),
            (s, 'i', 's7'), (s, 'i', 's7'),
            ('s1', 'u', 's2'), ('s1', 'U', 's2'),
            ('s2', 'e', 's3'), ('s2', 'E', 's3'),
            ('s3', 'v', 's4'), ('s3', 'V', 's4'),
            ('s4', 'o', 's5'), ('s4', 'O', 's5'),
            ('s5', ' ', 's6'), ('s5', ' ', 's6'),
            ('s6', 'i', 's7'), ('s6', 'I', 's7'),
            ('s7', 'n', 's8'), ('s7', 'N', 's8'),
            ('s8', 'i', 's9'), ('s8', 'I', 's9'),
            ('s9', 'c', 's10'), ('s9', 'C', 's10'),
            ('s10', 'i', 's11'), ('s10', 'I', 's11'),
            ('s11', 'o', 's12'), ('s11', 'O', 's12'),
            ('s12', ' ', 's13'), ('s12', ' ', 's13'),
            ('s13', 'd', 's14'), ('s13', 'D', 's14'),
            ('s14', 'e', 's15'), ('s14', 'E', 's15'),
            ('s15', ' ', 's16'), ('s15', ' ', 's16'),
            ('s16', 's', 's17'), ('s16', 'S', 's17'),
            ('s17', 'e', 's18'), ('s17', 'E', 's18'),
            ('s18', 's', 's19'), ('s18', 'S', 's19'),
            ('s19', 'i', 's20'), ('s19', 'I', 's20'),
            ('s20', 'ó', 's21'), ('s20', 'Ó', 's21'),
            ('s21', 'n', f), ('s21', 'N', f)
        ])

        # Confirmación de identidad
        self.identity_confirmation = copy.deepcopy(default_nfa)

        self.identity_confirmation.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'o', 's2'), ('s1', 'O', 's2'),
            ('s2', 'n', 's3'), ('s2', 'N', 's3'),
            ('s3', 'f', 's4'), ('s3', 'F', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'r', 's6'), ('s5', 'R', 's6'),
            ('s6', 'm', 's7'), ('s6', 'M', 's7'),
            ('s7', 'a', 's8'), ('s7', 'A', 's8'),
            ('s8', 'c', 's9'), ('s8', 'C', 's9'),
            ('s9', 'i', 's10'), ('s9', 'I', 's10'),
            ('s10', 'ó', 's11'), ('s10', 'Ó', 's11'),
            ('s11', 'n', 's12'), ('s11', 'N', 's12'),
            ('s12', ' ', 's13'), ('s12', ' ', 's13'),
            ('s12', ' ', 's17'), ('s12', ' ', 's17'),
            ('s13', 'd', 's14'), ('s13', 'D', 's14'),
            ('s14', 'e', 's15'), ('s14', 'E', 's15'),
            ('s15', ' ', 's16'), ('s15', ' ', 's16'),
            ('s16', 'i', 's17'), ('s16', 'I', 's17'),
            ('s17', 'd', 's18'), ('s17', 'D', 's18'),
            ('s18', 'e', 's19'), ('s18', 'E', 's19'),
            ('s19', 'n', 's20'), ('s19', 'N', 's20'),
            ('s20', 't', 's21'), ('s20', 'T', 's21'),
            ('s21', 'i', 's22'), ('s21', 'I', 's22'),
            ('s22', 'd', 's23'), ('s22', 'D', 's23'),
            ('s23', 'a', 's24'), ('s23', 'A', 's24'),
            ('s24', 'd', f), ('s24', 'D', f),
        ])

        self.unusual_activity = copy.deepcopy(default_nfa)

        # Actividad inusual
        self.unusual_activity.add_transitions([
            (s, 'a', 's1'), (s, 'A', 's1'),
            ('s1', 'c', 's2'), ('s1', 'C', 's2'),
            ('s2', 't', 's3'), ('s2', 'T', 's3'),
            ('s3', 'i', 's4'), ('s3', 'I', 's4'),
            ('s4', 'v', 's5'), ('s4', 'V', 's5'),
            ('s5', 'i', 's6'), ('s5', 'I', 's6'),
            ('s6', 'd', 's7'), ('s6', 'D', 's7'),
            ('s7', 'a', 's8'), ('s7', 'A', 's8'),
            ('s8', 'd', 's9'), ('s8', 'D', 's9'),
            ('s9', ' ', 's10'), ('s9', ' ', 's10'),
            ('s10', 'i', 's11'), ('s10', 'I', 's11'),
            ('s11', 'n', 's12'), ('s11', 'N', 's12'),
            ('s12', 'u', 's13'), ('s12', 'U', 's13'),
            ('s13', 's', 's14'), ('s13', 'S', 's14'),
            ('s14', 'u', 's15'), ('s14', 'U', 's15'),
            ('s15', 'a', 's16'), ('s15', 'A', 's16'),
            ('s16', 'l', f), ('s16', 'L', f),
        ])
        
        self.unusual_activity = copy.deepcopy(default_nfa)

        # Restaurar el acceso
        self.unusual_activity.add_transitions([
            (s, 'r', 's1'), (s, 'R', 's1'),
            ('s1', 'e', 's2'), ('s1', 'E', 's2'),
            ('s2', 's', 's3'), ('s2', 'S', 's3'),
            ('s3', 't', 's4'), ('s3', 'T', 's4'),
            ('s4', 'a', 's5'), ('s4', 'A', 's5'),
            ('s5', 'u', 's6'), ('s5', 'U', 's6'),
            ('s6', 'r', 's7'), ('s6', 'R', 's7'),
            ('s7', 'a', 's8'), ('s7', 'A', 's8'),
            ('s8', 'r', 's9'), ('s8', 'R', 's9'),
            ('s9', ' ', 's10'), ('s9', ' ', 's10'),
            ('s9', ' ', 's13'), ('s9', ' ', 's13'),
            ('s10', 'e', 's11'), ('s10', 'E', 's11'),
            ('s11', 'l', 's12'), ('s11', 'L', 's12'),
            ('s12', ' ', 's13'), ('s12', ' ', 's13'),
            ('s13', 'a', 's14'), ('s13', 'A', 's14'),
            ('s14', 'c', 's15'), ('s14', 'C', 's15'),
            ('s15', 'c', 's16'), ('s15', 'C', 's16'),
            ('s16', 'e', 's17'), ('s16', 'E', 's17'),
            ('s17', 's', 's18'), ('s17', 'S', 's18'),
            ('s18', 'o', f), ('s18', 'O', f),
])
        # Autenticación
        self.authentication = copy.deepcopy(default_nfa)

        self.authentication.add_transitions([
            (s, 'a', 's1'), (s, 'A', 's1'),
            ('s1', 'u', 's2'), ('s1', 'U', 's2'),
            ('s2', 't', 's3'), ('s2', 'T', 's3'),
            ('s3', 'e', 's4'), ('s3', 'E', 's4'),
            ('s4', 'n', 's5'), ('s4', 'N', 's5'),
            ('s5', 't', 's6'), ('s5', 'T', 's6'),
            ('s6', 'i', 's7'), ('s6', 'I', 's7'),
            ('s7', 'c', 's8'), ('s7', 'C', 's8'),
            ('s8', 'a', 's9'), ('s8', 'A', 's9'),
            ('s9', 'c', 's10'), ('s9', 'C', 's10'),
            ('s10', 'i', 's11'), ('s10', 'I', 's11'),
            ('s11', 'ó', 's12'), ('s11', 'Ó', 's12'),
            ('s12', 'n', f), ('s12', 'N', f)
        ])

    def __security_access_key(self, text):
        count = 0

        if (self.access_key.accepts(text)):
            count += 1

        return count

    def __security_authentication_code(self, text):
        count = 0

        if (self.authentication_code.accepts(text)):
            count += 1

        return count

    def __security_login_verification(self, text):
        count = 0

        if (self.login_verification.accepts(text)):
            count += 1

        return count

    def __security_identity_confirmation(self, text):
        count = 0

        if (self.identity_confirmation.accepts(text)):
            count += 1

        return count

    def __security_unusual_activity(self, text):
        count = 0

        if self.unusual_activity.accepts(text):
            count += 1

        return count

    def __security_authentication(self, text):
        count = 0

        if (self.authentication.accepts(text)):
            count += 1

        return count

    def execute(self, text):
        score = 0
        score += self.__security_access_key(text)
        score += self.__security_authentication_code(text)
        score += self.__security_login_verification(text)
        score += self.__security_identity_confirmation(text)
        score += self.__security_unusual_activity(text)
        score += self.__security_authentication(text)

        return score

class workClassification:

    def __init__(self, default_nfa, s, f):
        
        #Actualización de proyecto
        self.update_project = copy.deepcopy(default_nfa)

        self.update_project.add_transitions([
            (s, 'a', 's1'), (s, 'A', 's1'),
            ('s1', 'c', 's2'), ('s1', 'C', 's2'),
            ('s2', 't', 's3'), ('s2', 'T', 's3'),
            ('s3', 'u', 's4'), ('s3', 'U', 's4'),
            ('s4', 'a', 's5'), ('s4', 'A', 's5'),
            ('s5', 'l', 's6'), ('s5', 'L', 's6'),
            ('s6', 'i', 's7'), ('s6', 'I', 's7'),
            ('s7', 'z', 's8'), ('s7', 'Z', 's8'),
            ('s8', 'a', 's9'), ('s8', 'A', 's9'),
            ('s9', 'c', 's10'), ('s9', 'C', 's10'),
            ('s10', 'i', 's11'), ('s10', 'I', 's11'),
            ('s11', 'ó', 's12'), ('s11', 'Ó', 's12'),
            ('s12', 'n', 's13'), ('s12', 'N', 's13'),
            ('s13', ' ', 's14'), ('s13', ' ', 's14'),
            ('s14', 'd', 's15'), ('s14', 'D', 's15'),
            ('s15', 'e', 's16'), ('s15', 'E', 's16'),
            ('s16', ' ', 's17'), ('s16', ' ', 's17'),
            ('s17', 'p', 's18'), ('s17', 'P', 's18'),
            ('s18', 'r', 's19'), ('s18', 'R', 's19'),
            ('s19', 'o', 's20'), ('s19', 'O', 's20'),
            ('s20', 'y', 's21'), ('s20', 'Y', 's21'),
            ('s21', 'e', 's22'), ('s21', 'E', 's22'),
            ('s22', 'c', 's23'), ('s22', 'C', 's23'),
            ('s23', 't', 's24'), ('s23', 'T', 's24'),
            ('s24', 'o', f), ('s24', 'O', f),
        ])

        #Reporte de progreso
        self.progress_report = copy.deepcopy(default_nfa)

        self.progress_report.add_transitions([
            (s, 'r', 's1'), (s, 'R', 's1'),
            ('s1', 'e', 's2'), ('s1', 'E', 's2'),
            ('s2', 'p', 's3'), ('s2', 'P', 's3'),
            ('s3', 'o', 's4'), ('s3', 'O', 's4'),
            ('s4', 'r', 's5'), ('s4', 'R', 's5'),
            ('s5', 't', 's6'), ('s5', 'T', 's6'),
            ('s6', 'e', 's7'), ('s6', 'E', 's7'),
            ('s7', ' ', 's8'), ('s7', ' ', 's8'),
            ('s8', 'd', 's9'), ('s8', 'D', 's9'),
            ('s9', 'e', 's10'), ('s9', 'E', 's10'),
            ('s10', ' ', 's11'), ('s10', ' ', 's11'),
            ('s11', 'p', 's12'), ('s11', 'P', 's12'),
            ('s12', 'r', 's13'), ('s12', 'R', 's13'),
            ('s13', 'o', 's14'), ('s13', 'O', 's14'),
            ('s14', 'g', 's15'), ('s14', 'G', 's15'),
            ('s15', 'r', 's16'), ('s15', 'R', 's16'),
            ('s16', 'e', 's17'), ('s16', 'E', 's17'),
            ('s17', 's', 's18'), ('s17', 'S', 's18'),
            ('s18', 'o', f), ('s18', 'O', f)
        ])

        #Reunión de equipo
        self.team_meeting = copy.deepcopy(default_nfa)

        self.team_meeting.add_transitions([
            (s, 'r', 's1'), (s, 'R', 's1'),
            ('s1', 'e', 's2'), ('s1', 'E', 's2'),
            ('s2', 'u', 's3'), ('s2', 'U', 's3'),
            ('s3', 'n', 's4'), ('s3', 'N', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'ó', 's6'), ('s5', 'Ó', 's6'),
            ('s6', 'n', 's7'), ('s6', 'N', 's7'),
            ('s7', ' ', 's8'), ('s7', ' ', 's8'),
            ('s8', 'd', 's9'), ('s8', 'D', 's9'),
            ('s9', 'e', 's10'), ('s9', 'E', 's10'),
            ('s10', ' ', 's11'), ('s10', ' ', 's11'),
            ('s11', 'e', 's12'), ('s11', 'E', 's12'),
            ('s12', 'q', 's13'), ('s12', 'Q', 's13'),
            ('s13', 'u', 's14'), ('s13', 'U', 's14'),
            ('s14', 'i', 's15'), ('s14', 'I', 's15'),
            ('s15', 'p', 's16'), ('s15', 'P', 's16'),
            ('s16', 'o', f), ('s16', 'O', f)
        ])

        #Asignación de tareas
        self.task_assignment = copy.deepcopy(default_nfa)

        self.task_assignment.add_transitions([
            (s, 'a', 's1'), (s, 'A', 's1'),
            ('s1', 's', 's2'), ('s1', 'S', 's2'),
            ('s2', 'i', 's3'), ('s2', 'I', 's3'),
            ('s3', 'g', 's4'), ('s3', 'G', 's4'),
            ('s4', 'n', 's5'), ('s4', 'N', 's5'),
            ('s5', 'a', 's6'), ('s5', 'A', 's6'),
            ('s6', 'c', 's7'), ('s6', 'C', 's7'),
            ('s7', 'i', 's8'), ('s7', 'I', 's8'),
            ('s8', 'ó', 's9'), ('s8', 'Ó', 's9'),
            ('s9', 'n', 's10'), ('s9', 'N', 's10'),
            ('s10', ' ', 's11'), ('s10', ' ', 's11'),
            ('s11', 'd', 's12'), ('s11', 'D', 's12'),
            ('s12', 'e', 's13'), ('s12', 'E', 's13'),
            ('s13', ' ', 's14'), ('s13', ' ', 's14'),
            ('s14', 't', 's15'), ('s14', 'T', 's15'),
            ('s15', 'a', 's16'), ('s15', 'A', 's16'),
            ('s16', 'r', 's17'), ('s16', 'R', 's17'),
            ('s17', 'e', 's18'), ('s17', 'E', 's18'),
            ('s18', 'a', 's19'), ('s18', 'S', 's19'),
            ('s19', 's', f), ('s19', 'S', f)
        ])


        #Cambio en políticas
        self.policy_change = copy.deepcopy(default_nfa)

        self.policy_change.add_transitions([
            (s, 'c', 's1'), (s, 'C', 's1'),
            ('s1', 'a', 's2'), ('s1', 'A', 's2'),
            ('s2', 'm', 's3'), ('s2', 'M', 's3'),
            ('s3', 'b', 's4'), ('s3', 'B', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'o', 's6'), ('s5', 'O', 's6'),
            ('s6', ' ', 's7'), ('s6', ' ', 's7'),
            ('s7', 'e', 's8'), ('s7', 'E', 's8'),
            ('s8', 'n', 's9'), ('s8', 'N', 's9'),
            ('s9', ' ', 's10'), ('s9', ' ', 's10'),
            ('s10', 'p', 's11'), ('s10', 'P', 's11'),
            ('s11', 'o', 's12'), ('s11', 'O', 's12'),
            ('s12', 'l', 's13'), ('s12', 'L', 's13'),
            ('s13', 'í', 's14'), ('s13', 'Í', 's14'),
            ('s14', 't', 's15'), ('s14', 'T', 's15'),
            ('s15', 'i', 's16'), ('s15', 'I', 's16'),
            ('s16', 'c', 's17'), ('s16', 'C', 's17'),
            ('s17', 'a', 's18'), ('s17', 'A', 's18'),
            ('s18', 's', f), ('s18', 'S', f)
        ])

        # Proyecto
        self.project = copy.deepcopy(default_nfa)

        self.project.add_transitions([
            (s, 'p', 's1'), (s, 'P', 's1'),
            ('s1', 'r', 's2'), ('s1', 'R', 's2'),
            ('s2', 'o', 's3'), ('s2', 'O', 's3'),
            ('s3', 'y', 's4'), ('s3', 'Y', 's4'),
            ('s4', 'e', 's5'), ('s4', 'E', 's5'),
            ('s5', 'c', 's6'), ('s5', 'C', 's6'),
            ('s6', 't', 's7'), ('s6', 'T', 's7'),
            ('s7', 'o', f), ('s7', 'O', f)
        ])

        # Reunión
        self.meeting = copy.deepcopy(default_nfa)

        self.meeting.add_transitions([
            (s, 'r', 's1'), (s, 'R', 's1'),
            ('s1', 'e', 's2'), ('s1', 'E', 's2'),
            ('s2', 'u', 's3'), ('s2', 'U', 's3'),
            ('s3', 'n', 's4'), ('s3', 'N', 's4'),
            ('s4', 'i', 's5'), ('s4', 'I', 's5'),
            ('s5', 'ó', 's6'), ('s5', 'Ó', 's6'),
            ('s6', 'n', f), ('s6', 'N', f)
        ])

    def __work_update_project(self, text):
        count = 0

        if (self.update_project.accepts(text)):
            count += 1

        return count
    
    def __work_progress_report(self, text):
        count = 0

        if (self.progress_report.accepts(text)):
            count += 1

        return count
    
    def __work_team_meeting(self, text):
        count = 0

        if (self.team_meeting.accepts(text)):
            count += 1

        return count
    
    def __work_task_assignment(self, text):
        count = 0

        if (self.task_assignment.accepts(text)):
            count += 1

        return count
    
    def __work_policy_change(self, text):
        count = 0

        if (self.policy_change.accepts(text)):
            count += 1

        return count
    
    def __work_project(self, text):
        count = 0

        if (self.project.accepts(text)):
            count += 1

        return count
    
    def __work_meeting(self, text):
        count = 0

        if (self.meeting.accepts(text)):
            count += 1

        return count
    
    def execute(self, text):
        score = 0
        score += self.__work_update_project(text)
        score += self.__work_progress_report(text)
        score += self.__work_team_meeting(text)
        score += self.__work_task_assignment(text)
        score += self.__work_policy_change(text)
        score += self.__work_project(text)
        score += self.__work_meeting(text)

        return score

class Classification:
    s = State('s0')
    f = State('f0')
    default_transitions = [
        (s, Symbol(' '), s),
        (s, Symbol('\n'), s),
        (f, Symbol(' '), f),
        (f, Symbol('\n'), f),
    ]

    for c in range(ord("a"), ord("z") + 1):
        default_transitions.append((s, Symbol(chr(c)), s))
        default_transitions.append((f, Symbol(chr(c)), f))

    for c in range(ord("A"), ord("Z") + 1):
        default_transitions.append((s, Symbol(chr(c)), s))
        default_transitions.append((f, Symbol(chr(c)), f))

    for c in range(10):
        default_transitions.append((s, Symbol(f"{c}"), s))
        default_transitions.append((f, Symbol(f"{c}"), f))

    for c in ["@",".","_","'","\"","-",",",";",":","(",")","[","]","{","}","<",">","¡","¿","ñ","Ñ","á","é","í","ó","ú","Á","É","Í","Ó","Ú","\\","/","&","%","$","#","*","+","^","`","~","|","!","?"]:
        default_transitions.append((s, Symbol(c), s))
        default_transitions.append((f, Symbol(c), f))

    default_nfa = NondeterministicFiniteAutomaton()
    default_nfa.add_transitions(default_transitions)
    default_nfa.add_start_state(s)
    default_nfa.add_final_state(f)

    def __init__(self):
        self.spam = SpamClassification(self.default_nfa, self.s, self.f)
        self.invitation = InvitationClassification(self.default_nfa, self.s, self.f)
        self.security = SecurityClassification(self.default_nfa, self.s, self.f)
        self.work = workClassification(self.default_nfa, self.s, self.f)

    def execute(self, text):
        return pd.DataFrame(
            {
                "SPAM": self.spam.execute(text),
                "INVITACIÓN": self.invitation.execute(text),
                "SEGURIDAD": self.security.execute(text),
                "TRABAJO": self.work.execute(text),
                "OTRO": 1
            },
            index=[0],
        )
