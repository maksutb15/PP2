�
    ��eN  �                   �0   � d Z ddlZd� Zedk(  r e�        yy)a�  
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
�    Nc                  �.  � t        d�       t        �       } t        d| � d��       t        j                  dd�      }d}	 t        d�       t	        t        �       �      }|dz  }||k  rt        d�       n$||kD  rt        d	�       nt        d
| � d|� d��       y �Y)NzHello! What is your name?zWell, z-, I am thinking of a number between 1 and 20.�   �   r   zTake a guess.zYour guess is too low.zYour guess is too high.z
Good job, z! You guessed my number in z	 guesses!)�print�input�random�randint�int)�name�secret_number�guesses_taken�guesss       �1c:\Users\1\Desktop\PP2\Lab3\01_functions1\ex13.py�guess_the_numberr      s�   � �	�
%�&��7�D�	�F�4�&�E�
F�G��N�N�1�b�)�M��M�
��o���E�G��������=� ��*�+��]�"��+�,��J�t�f�$?���i�X�Y�� �    �__main__)�__doc__r   r   �__name__� r   r   �<module>r      s)   ���* ��* �z���� r   