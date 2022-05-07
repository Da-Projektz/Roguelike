<div align="center"><h2>Rougue-ish<br>the colours of blood</h1></div>

### Git workflow
*Recommended*
1. Clone the repository
2. Stage and commit changes to `main`
3. Push to a new branch like so:
   ```sh
   git push origin main:<branch-name>
   ```

*Alternative*
- **Don't push to main**:w
- Push to a *branch* of main!

1. Clone
2. Create a spin-off branch of origin/main
3. Stage changes and commit
4. Push to origin, creating the branch.

### Adding new features
1. Create a card in the project
2. Convert it to an issue
3. Commit your changes with a commit summary/title with the special wording:
   
   `fix #<issue-number>`
   
   This causes the PR containing the commit to 'track' with the issue it states it will "fix" or "fixes" (please prefer 'fix'). When the PR is merged it will automatically resolve the issue.