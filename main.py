import asyncio
import random


warehouse = []

max_elements = 10


def is_overflow() -> bool:
    """Проверка на переполнение склада"""
    return len(warehouse) >= max_elements


def is_underflow() -> bool:
    """Проверка склада на пустоту можно ли забирать из него товар"""
    return len(warehouse) == 0


async def producer(id: int) -> None:
    """Имитация производителя пополняющего товарный склад"""
    while True:
        num_of_product = random.randint(a=1, b=10000)
        print(f'Производитель номер {id} произвел товар номер {num_of_product}')
        if not is_overflow():
            warehouse.append(num_of_product)
        else:
            print(f"Переполнение. Производитель {id} ждет чтобы произвести и сложить в склад")
        await asyncio.sleep(random.random() * 5.0)


async def consumer(id: int) -> None:
    """Имитация потребителей берущих все со склада при наличии товара"""
    while True:
        if not is_underflow():
            num_of_product = warehouse.pop(0)
            print(f"Потребитель номер {id} забрал товар номер {num_of_product}")
        else:
            print(f"Недополнение. Потребитель {id} ждет товар на складе")
        await asyncio.sleep(random.random() * 2.0)


async def main() -> None:
    """Запуск produces и consumers асинхронно"""
    task_producer1 = asyncio.create_task(producer(1))
    task_producer2 = asyncio.create_task(producer(2))

    task_consumer1 = asyncio.create_task(consumer(1))
    task_consumer2 = asyncio.create_task(consumer(2))
    task_consumer3 = asyncio.create_task(consumer(3))
    task_consumer4 = asyncio.create_task(consumer(4))
    task_consumer5 = asyncio.create_task(consumer(5))
    task_consumer6 = asyncio.create_task(consumer(6))

    await task_producer1
    await task_producer2
    await task_consumer1
    await task_consumer2
    await task_consumer3
    await task_consumer4
    await task_consumer5
    await task_consumer6

asyncio.run(main())

