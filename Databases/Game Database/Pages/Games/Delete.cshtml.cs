﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using GameDatabase.Data;
using GameDatabase.Models;

namespace GameDatabase.Pages.Games
{
    public class DeleteModel : PageModel
    {
        private readonly GameDatabase.Data.GameDatabaseContext _context;

        public DeleteModel(GameDatabase.Data.GameDatabaseContext context)
        {
            _context = context;
        }

        [BindProperty]
      public Game Game { get; set; } = default!;

        public async Task<IActionResult> OnGetAsync(int? id)
        {
            if (id == null || _context.Game == null)
            {
                return NotFound();
            }

            var game = await _context.Game.FirstOrDefaultAsync(m => m.Id == id);

            if (game == null)
            {
                return NotFound();
            }
            else 
            {
                Game = game;
            }
            return Page();
        }

        public async Task<IActionResult> OnPostAsync(int? id)
        {
            if (id == null || _context.Game == null)
            {
                return NotFound();
            }
            var game = await _context.Game.FindAsync(id);

            if (game != null)
            {
                Game = game;
                _context.Game.Remove(Game);
                await _context.SaveChangesAsync();
            }

            return RedirectToPage("./Index");
        }
    }
}