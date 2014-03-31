import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 */

/**
 * @author Zach
 *
 */
public class Hangman {

	private String word;
	private ArrayList<Character> guessedLetters;
	private char[] puzzle;
	private int incorrectGuesses;
	static ArrayList<String> allWords = null;
	
	public Hangman(String filename) {
		setRandomWord(filename);
	}
	public void setWord(String word) {
		word = word.replaceAll("[^a-zA-Z ]", "").toLowerCase();
		this.puzzle = new char[word.length()];
		emptyPuzzle();
		this.incorrectGuesses = 0;
		this.guessedLetters = new ArrayList<Character>();
		this.word = word;
	}
	public String getWord() {
		return this.word;
	}
	private void emptyPuzzle() {
		for(int i = 0; i < puzzle.length; i++) {
			this.puzzle[i] = '_';
		}
	}
	public void setPuzzle(char[] puzzle) {
		this.puzzle = puzzle;
	}
	public char[] getPuzzle() {
		//The puzzle is in the format of ["_","_","_","_"] for a 4-length word
		return this.puzzle;
	}
	public void setIncorrectGuesses(int guesses) {
		this.incorrectGuesses = guesses;
	}
	public int getIncorrectGuesses() {
		return this.incorrectGuesses;
	}
	public void setRandomWord(String filename) {
		ArrayList<String> allWords = getAllWords(filename);
		int wordIndex = (int) (Math.random() * allWords.size());
		setWord(allWords.get(wordIndex));
	}
	private static ArrayList<String> getAllWords(String filename) {
		if (allWords != null) {
			return allWords;
		}
		ArrayList<String> allWords = new ArrayList<String>();
		File wordsFile = new File(filename);
		Scanner fileIn;
		try {
			fileIn = new Scanner(wordsFile);
			while (fileIn.hasNext()) {
				allWords.add(fileIn.next());
			}
			fileIn.close();
		}
		catch (FileNotFoundException e) {
			System.out.println("File " + filename + " not found in " + System.getProperty("user.dir"));
			System.out.println(e);
			System.exit(0);
			return allWords;
		}
		return allWords;
	}
	public boolean guessLetter(char letter) {
		boolean correctGuess = false;
		if (this.guessedLetters.contains(letter)) {
			return false; //We've already guessed this letter
		}
		guessedLetters.add(letter);
		for (int i = 0; i < this.word.length(); i++) {
			if (this.word.charAt(i) == letter) {
				this.puzzle[i] = letter;
				correctGuess = true;
			}
		}
		if (!correctGuess) {
			this.incorrectGuesses++;
		}
		return correctGuess;
	}
	public boolean isSolved() {
		for (int i = 0; i < this.puzzle.length; i++) {
			if (puzzle[i] == '_') {
				return false;
			}
		}
		return true;
	}

}
