def align_yaxes_grid(ax_ref, ax_tgt):
  """Aligns the grid of two y-axes.
  
  Corrects that strange visual when two twin axes have
  unaligned vertical grid lines. It will replicate the
  structure of a given reference axis (`ax_ref`) to a
  target axis (`ax_tgt`), keeping the target's first and
  last visible ticks. Other target ticks may be changed
  to ensure the same number of grid lines in both axes.
  """
  
  # visible limit in the picture
  limit_ref = np.array(ax_ref.get_ylim())
  limit_old = np.array(ax_tgt.get_ylim())
  # all y-axis ticks: those visible plus 2 out of bouonds
  ticks_ref = np.array(ax_ref.get_yticks())
  ticks_old = np.array(ax_tgt.get_yticks())
  # the first and last ticks visible
  marks_ref = ticks_ref[[1, -2]]
  marks_old = ticks_old[[1, -2]]
  # central point foir alignment
  center_ref = np.mean(marks_ref)
  center_old = np.mean(marks_old)
  # distance between marks
  range_ref = np.diff(marks_ref)
  range_old = np.diff(marks_old)
  # rescale the target (old) limit and ticks arrays by the reference axis
  limit_new = (limit_ref - center_ref) * (range_old / range_ref) + center_old
  ticks_new = (ticks_ref - center_ref) * (range_old / range_ref) + center_old
  # update the values
  ax_tgt.set_yticks(ticks_new)
  ax_tgt.set_ylim(limit_new)
