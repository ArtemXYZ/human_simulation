"""Базовая реализация нейрона."""

import numpy as np
from abc import ABC, abstractmethod
# ----------------------------------------------------------------------------------------------------------------------

# Вот базовый код, который можно использовать как основу:

# Абстрактный класс для нейрона
class Neuron(ABC):
    def __init__(self, weights, bias):
        self.weights = np.array(weights)
        self.bias = bias
        self.input_signal = None  # Место для хранения входного сигнала
        self.output_signal = None  # Место для хранения выходного сигнала

    # Метод активации (возможна замена в дочерних классах)
    def activation(self, signal_sum):
        return max(0, signal_sum)  # Функция ReLU как базовая реализация

    # Абстрактный метод для feedforward
    @abstractmethod
    def feedforward(self, inputs):
        pass

    # Метод для расчета выхода (общий для всех нейронов)
    def process_input(self, inputs):
        self.input_signal = np.array(inputs)
        signal_sum = np.dot(self.input_signal, self.weights) + self.bias
        self.output_signal = self.activation(signal_sum)
        return self.output_signal

# Класс для центростремительных  (афферентных (сенсорных))  нейронов
class AfferentNeuron(Neuron):
    def __init__(self, weights, bias):
        super().__init__(weights, bias)

    # Специфическая реализация feedforward для сенсорных нейронов
    def feedforward(self, external_stimulus):
        print("Processing external stimulus...")
        return self.process_input(external_stimulus)

# Класс для центробежных (эфферентных (моторных)) нейронов
class EfferentNeuron(Neuron):
    def __init__(self, weights, bias):
        super().__init__(weights, bias)


    # Специфическая реализация feedforward для моторных нейронов
    def feedforward(self, processed_signal):
        print("Sending signal to execute action...")
        return self.process_input(processed_signal)



# Класс для интернейронов (вставочных нейронов)
class Interneuron(Neuron):
    def __init__(self, weights, bias):
        super().__init__(weights, bias)

    # Специфическая реализация feedforward для вставочных нейронов
    def feedforward(self, inputs):
        print("Relaying signal between neurons...")
        return self.process_input(inputs)






# # Пример использования
# weights = [0.5, 0.3, 0.2]  # Пример весов
# bias = 0.1  # Пример смещения
# stimulus = [0.6, 0.4, 0.2]  # Пример входного стимула
#
# # Создание экземпляров нейронов
# afferent_neuron = AfferentNeuron(weights, bias)
# interneuron = Interneuron(weights, bias)
# efferent_neuron = EfferentNeuron(weights, bias)
#
# # Симуляция передачи сигнала
# afferent_output = afferent_neuron.feedforward(stimulus)
# print(f"Afferent output: {afferent_output}")
#
# interneuron_output = interneuron.feedforward(afferent_output)
# print(f"Interneuron output: {interneuron_output}")
#
# efferent_output = efferent_neuron.feedforward(interneuron_output)
# print(f"Efferent output: {efferent_output}")









# ----------------------------------------------------------------------------------------------------------------------

# # Класс для одного нейрона
# class Neuron:
#     """
#     Bias (смещение).
#     Термин bias стал стандартом в мире искусственных нейронных сетей, суть его работы — это сдвиг функции активации \
#     (в литературе принято называть этот параметр именно bias).
#     Bias — это дополнительный параметр в нейронной сети, который добавляется к взвешенной сумме входных сигналов.
#
#     Физическое значение bias:
# 	В биологических нейронах это эквивалентно пороговому значению, которое необходимо достичь,\
# 	чтобы нейрон активировался. Нейрон не активируется, пока сумма входящих сигналов не превысит определенный порог.
# 	Bias позволяет нейрону "сдвинуть" функцию активации вверх или вниз, что помогает сети лучше моделировать сложные \
# 	зависимости между входами и выходами. Это делает нейрон более чувствительным к слабым или сильным сигналам.
#     """
#
#
#     def __init__(self, weights, bias):
#         """
#
#         :param weights: Веса (массив входных импульсов (весов)), которые нейрон использует для оценки важности
#         каждого входного сигнала. Они соответствуют силе связи с каждым входом.
#         :param bias:
#         """
#
#         self.weights = weights
#         self.bias = bias  # Смещение
#
#     def activation(self, x):
#         """
#         Физическое значение:
#         Активационная функция в биологических нейронах моделирует процесс принятия решения нейроном: \
#         активируется ли он (выдаст ли сигнал дальше), в зависимости от силы входного сигнала.
#
#         Функция принимает значение x, которое может быть результатом взвешенной суммы входов.
#         Затем она использует функцию ReLU (Rectified Linear Unit), которая возвращает максимум между нулем \
#         и этим значением.
#         Если значение x положительное, оно остается без изменений. Если x отрицательное, оно становится 0.
#
#         :param x:
#         :return:
#         """
#
#         # В данном примере используем ReLU в качестве активационной функции
#         return np.maximum(0, x)
#
#     def feedforward(self, inputs):   # прямая связь
#         """
#
#         :param inputs: Входной параметр, массив чисел (сигналы от других нейронов или сенсоров).
#
#         :return: Финальный результат работы нейрона — это активированное значение, которое передается
#          на следующий слой сети или используется в текущем процессе.
#
#         Вычисления взвешенной суммы. Это аналог внутреннего произведения вектора входных данных и вектора весов.
#         После вычисления взвешенной суммы, добавляется смещение (bias). Bias можно представить как базовый порог,
#         который нейрон должен "перешагнуть", чтобы быть активированным.
#         Это позволяет нейрону быть активным, даже если входные сигналы не очень сильные
#         (например, входы могут быть равны нулю, но bias будет обеспечивать некое минимальное значение).
#
#         Активация.
#         После вычисления итоговой суммы (взвешенные входы + bias), результат передается в метод self.activation(total),
#         который пропускает это значение через активационную функцию (в данном случае через ReLU).
#         Активационная функция "решает", будет ли нейрон активирован, и какое значение он передаст дальше.
#         """
#
#         # Вычисляем взвешенную сумму входов и добавляем bias
#         total = np.dot(self.weights, inputs) + self.bias
#         # Пропускаем через активационную функцию
#         return self.activation(total)



# # Пример использования нейрона
# weights = np.array([0.5, 0.3, 0.2])  # Веса нейрона
# bias = 0.7  # Смещение (bias)
# neuron = Neuron(weights, bias)
#
# inputs = np.array([1, 2, 3])  # Входные данные
# output = neuron.feedforward(inputs)  # Передача данных через нейрон
# print("Выход нейрона:", output)