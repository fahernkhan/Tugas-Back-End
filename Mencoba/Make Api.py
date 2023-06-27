import queue
import time

def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            print(f"Task {name} running")
            time.sleep(count)

def main():
    """
    Ini adalah fungsi utama pada program
    """
    # Buat fungsi antrian
    work_queue = queue.Queue()
    # Masukkan pekerjaan ke dalam antrian 
    for work in [5, 3, 2, 1]:
        work_queue.put(work)
    # Buat sebuah pekerjaan berbasis synchronous dengan menggunakan fungsi pertama
    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
    # Jalankan antrian pekerjaan
    for t, n, q in tasks:
        t(n, q)

if __name__ == "__main__":
    main()


#diubah ke bentuk async----------------------------------------------------------------------------------
import queue
import asyncio

async def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            delay = await work_queue.get()
            print(f"Task {name} running")
            await asyncio.sleep(delay)

async def main():
    """
    Ini adalah fungsi utama pada program
    """
    # Buat fungsi antrian
    work_queue = asyncio.Queue()
    # Masukkan pekerjaan ke dalam antrian 
    for work in [5, 3, 2, 1]:
        await work_queue.put(work)
       
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )

if __name__ == "__main__":
    asyncio.run(main())