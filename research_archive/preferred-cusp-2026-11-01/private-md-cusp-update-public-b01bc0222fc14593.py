from pathlib import Path
import json
root=Path('/private/tmp/murakamis_dream-publication')
changed=[]
def replace(rel, old, new):
    p=root/rel;s=p.read_text();assert old in s,(rel,old[:100]);p.write_text(s.replace(old,new,1));changed.append(rel)
replace('notes/actual_main_meridian_filled_volume.md',
'Section 2 fixes this normalization and defines an explicit scalar \\(A_N(s)\\) from the original finite compiler.',
'Section 2 fixes this normalization. The exact scalar from the original finite compiler is\n\\[\n A_N(s)=q_N^{a(D)s^2/2},\\qquad\n a(D)=-w(D)-\\sum_i n_i,\n\\]\nwhere \\(w(D)\\) is the oriented writhe of the filled diagram, and each \\(n_i\\) uses the original checked-braid convention.')
replace('notes/actual_main_meridian_filled_volume.md',
'Formula (7) makes no identification with a cusp shape or with a classical \\(A\\)-polynomial factor.',
r'''The [preferred-longitude calculation](actual_main_meridian_preferred_cusp.md) identifies the full first correction geometrically. In the meridian-longitude basis of the knot complement, let \(\tau_K\) be the translation of the preferred longitude when the meridian translates by one. Then
\[
 \tau_K=a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}}).
 \tag{7a}
\]
Combining (7a) with the exact scalar above gives
\[
 \boxed{\displaystyle
 \frac{F_N(q_N^s)}{F_N(1)H_N(s)}
 =1+\frac{\pi i s^2\tau_K}{2N}
                 +O_{\mathbf n,R}(N^{-2}).}
 \tag{7b}
\]
This is also the normalized profile of the full modified-trace invariant, by (12). The geometric proof of (7a) applies to the broader strict-tree class; the asymptotic (7b) retains the component condition of this theorem. Neither statement identifies a classical \(A\)-polynomial factor.''')
replace('notes/actual_main_meridian_filled_volume.md',
'These statements follow from the original scalar formulas, not from a bound on the unknown knot invariant. The other factors in (15) and their inverses are uniformly bounded on every fixed disk. Keeping \\(A_N\\) exact is stronger and safer than silently replacing it by one.',
r'''These bounds follow from the original scalar formulas. The [exact scalar calculation](actual_main_meridian_exact_scalar.md) simplifies their complete product:
\[
 A_N(s)=q_N^{[-w(D)-\sum_i n_i]s^2/2}.
 \tag{16f}
\]
It proves the cancellation of all intermediate turn factors and the remaining closing factor separately. Thus \(A_N(s)\to1\) uniformly on each fixed microscopic disk. Keeping its first term is necessary for (7b): it supplies the integer part of the preferred cusp shape.''')
replace('notes/actual_main_meridian_filled_volume.md',
'This is merely a coordinate rewrite. It does not identify the sum, or the sum together with the exact scalar ledger, with the main-cusp modulus. Such an identification requires a separate comparison of the original main peripheral deformation.',
r'''The exact scalar contributes \(a(D)z^2/(8\pi iN)\). The [geometric longitude theorem](actual_main_meridian_preferred_cusp.md) identifies its sum with (44) as \(\tau_Kz^2/(8\pi iN)\), proving (7b). The two calculations are independent: the quantum calculation fixes the scalar, and the geometric calculation follows the actual longitude through the face pairings and disk fillings. The reduced ratio consequently tends to \(\sin(\pi s)/(\pi s)\) without an additional scalar normalization. The normalized full modified-trace invariant tends to one.''')
replace('book/chapters/results.md',
'The passage through ordinary-color resonances and the identification\nof the correction with the preferred cusp shape are results for the\nfigure-eight knot. The Conway theorem below gives a moving-meridian\nprofile on a smaller disk, before those resonances.',
'The passage through ordinary-color resonances in this form is a result\nfor the figure-eight knot. The Conway theorem below gives a moving-meridian\nprofile and a preferred-cusp correction on a smaller disk, before those resonances.')
replace('book/chapters/results.md',
'The proof gives more than logarithmic growth. Let \\(A_N(s)\\) be the explicitly prescribed scalar obtained from the strand orientations, crossing powers, bends and zero-framing correction. It is calculated from those finite operations, before evaluating the invariant. Then',
r'''The proof gives more than logarithmic growth. The original crossing and framing factors have an exact combined value:
\[
 A_N(s)=q_N^{a(D)s^2/2},\qquad
 a(D)=-w(D)-\sum_i n_i.
\]
Here \(w(D)\) is the oriented writhe, and each \(n_i\) is the signed crossing power in its original braid box. The [scalar calculation](../../notes/actual_main_meridian_exact_scalar.md) derives this from the finite tangle operations. Then''')
replace('book/chapters/results.md',
'with the value one assigned to the displayed quotient at \\(s=0\\). After this exact normalization, the profile tends to \\(\\sin(\\pi s)/(\\pi s)\\). Section 2 of the theorem lists the scalar factors, including the different factors for the two orders of oppositely directed strands. Keeping them is necessary even though they do not change the logarithmic volume.',
'with the value one assigned to the sine quotient at \\(s=0\\). Since \\(A_N(s)\\) tends uniformly to one, the reduced ratio \\(F_N(q_N^s)/F_N(1)\\) itself tends to \\(\\sin(\\pi s)/(\\pi s)\\). The scalar still contributes to the first correction below.')
replace('book/chapters/results.md',
'The theorem also computes the first correction after division by \\(A_N(s)\\) and the sine quotient. Its geometric interpretation as a preferred cusp shape has not been established for this class. Nor does the argument pass through \\(s=\\pm1\\), the first ordinary-color resonances, or identify a classical geometric factor of the quantum recurrence.',
r'''The first correction records the shape of the knot cusp. A horospherical cross-section is a Euclidean torus. Choose its coordinate so that the meridian translates by one, and write \(\tau_K\) for the translation of the preferred longitude, the curve with zero linking number with the knot. With
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},
\]
the result is
\[
 \frac{F_N(q_N^s)}{F_N(1)H_N(s)}
 =1+\frac{\pi i s^2\tau_K}{2N}+O(N^{-2}).
\]
The [geometric proof](../../notes/actual_main_meridian_preferred_cusp.md) computes this longitude from the original face identifications and corrects its marking after surgery on the crossing circles. It does not infer the cusp shape from the asymptotic formula. The full modified-trace invariant has exactly the displayed normalized profile because its modified dimension cancels \(H_N\).

The geometric longitude identity holds for all the strict presentations considered there. This asymptotic still has the additional junction condition stated above. Passage through \(s=\pm1\), the first ordinary-color resonances, and identification of a classical geometric factor of the quantum recurrence remain open for this class.''')
replace('book/chapters/frontier.md',
'Three distinctions remain essential. First, this stronger result has the extra component condition; the complete-value theorem at \\(M=1\\) retains its broader scope. Second, the disk shrinks like \\(1/N\\) in \\(M\\), so this does not contradict the nearby zeros described above. Third, the first correction is computed from the complex edge labels of the filled critical point, but has not been identified with the preferred main-cusp modulus.',
r'''The [longitude calculation](../../notes/actual_main_meridian_preferred_cusp.md) now identifies the first correction with the preferred cusp shape \(\tau_K\). After division by the displayed sine quotient, the normalized invariant equals
\[
 1+\frac{\pi i s^2\tau_K}{2N}+O(N^{-2}).
\]
The [exact scalar calculation](../../notes/actual_main_meridian_exact_scalar.md) supplies the integer framing term; the geometric proof determines the same term from the longitude and the auxiliary surgery. The geometric identity holds for the broader strict-tree class. The asymptotic still requires the extra component condition, and its disk still shrinks like \(1/N\) in \(M\). The complete-value theorem retains its broader scope.''')
replace('book/chapters/index.md',
'After the prescribed framing and orientation factors are removed, the ratio to the complete value tends to \\(\\sin(\\pi s)/(\\pi s)\\).',
'The ratio to the complete value tends to \\(\\sin(\\pi s)/(\\pi s)\\), and the first correction after division by the exact sine quotient is determined by the preferred cusp shape.')
replace('README.md',
'and an explicit normalized profile for long-twist presentations satisfying\nan additional condition on their multiplication junctions.',
'and an explicit normalized profile for long-twist presentations satisfying\nan additional condition on their multiplication junctions. The first\ncorrection is determined by the preferred cusp shape; a separate geometric\ncalculation follows the longitude through the crossing-circle surgeries.')
Path('/private/tmp/md-cusp-initial-changed.json').write_text(json.dumps(sorted(set(changed)),indent=2)+'\n')
print(json.dumps({'changed':sorted(set(changed))}))
