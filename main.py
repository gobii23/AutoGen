# import time

# def brew_cofee():
#     print("Brewing coffee...")
#     time.sleep(5)
#     print("Coffee is ready!")

# def toast_bread():
#     print("Toasting bread...")
#     time.sleep(3)
#     print("Bread is toasted!")
    
# def main():
#     start = time.time()
#     coffee = brew_cofee()
#     bread = toast_bread()
#     end = time.time()
#     print(f"Total time taken: {end - start:.2f} seconds")

# main()



import time
import asyncio

async def brew_coffee():
    print("Brewing coffee...")
    await asyncio.sleep(5)
    print("Coffee is ready!")

async def toast_bread():
    print("Toasting bread...")
    await asyncio.sleep(3)
    print("Bread is toasted!")

async def main():
    start = time.time()
    coffee = brew_coffee()
    bread = toast_bread()
    results =  await asyncio.gather(coffee, bread)
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")

asyncio.run(main())

