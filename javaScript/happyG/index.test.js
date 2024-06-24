const gHappy = require("./index.js")

describe("index.js", ()=>{
  it("Will test the gHappy function with the input of 'gg0gg3gg0gg'", ()=>{
    expect(gHappy("gg0gg3gg0gg")).toBe(true)
  })
  
  it("Will test the gHappy function with the input of 'gog'",()=>{
    expect(gHappy("gog")).toBe(false)
  })
  
  it("gHappy with the input of 'ggg ggg g ggg'", ()=>{
    expect(gHappy("ggg ggg g ggg")).toBe(false)
  })
  
  it("gHappy with an input string of no g's", ()=>{
    expect(gHappy("A half of a half is a quarter")).toBe(true)
  })
  
  it("gHappy with g's located apart from each other in separate words", ()=>{
    expect(gHappy("good grief")).toBe(false)
  })

  it("gHappy with coupled g's within separate strings", ()=>{
    expect(gHappy("bigger is ggooder")).toBe(true)
  })

  it("gHappy will contain an even number of g's", ()=> {
    expect(gHappy("gggggggggggg")).toBe(true)
  })
})