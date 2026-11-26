# Extending the complete lower integration interval to one half

Research proof, 8 November 2026. The entire first incoming integral
has a strict upper bound when the next real boundary coordinate
ranges from \(9/20\) to \(1/2\), at its original negative height.
This interval can consequently be removed from the remaining
signed contour. The proof below assembles estimates for all parts
of the first incoming cycle, then checks the original Fourier
filter and its denominator.

The statement concerns an ordinary next vertex after the prefix
\((3,4)\). It leaves the other lower intervals and both remaining
upper intervals explicit. No numerical evaluation or modification
of a frozen source is used.

## 1. Source, parameters and complete first cycle

Retain the canonical ordinary-next reference family of
[the complete lower central interval](research_mixed_next_complete_lower_plateau.md),
Section 1. Write
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3),\qquad
 h_a=\Im a_*,\quad h_y=\Im y_*,\quad \alpha=\Re y_* .
 \tag{1}
\]
The flags are \((0,1,\beta)\), with \(\beta=0,1\). Both vertices
after the first cap are ordinary, and the last typed input
retains its original correlations. In particular
\[
 -.102<h_y<-.001,\qquad .24<\alpha<.36 .
\]
Let
\[
 P=[.22,.45],\qquad J_{\rm sh}=[.45,.5],\qquad
 y=q+ih_y,\quad q\in J_{\rm sh},\qquad
 z=u+i\Im z_*,\quad u\in P,
 \quad Y=e^{-2\pi iy},\ Z=e^{-2\pi iz}.
 \tag{2}
\]
The subscript on \(J_{\rm sh}\) labels this particular boundary
interval; it is not an additional contour choice.

For \(r=e^{-2\pi i/N}\), define \(P_j=(r;r)_j\) and
\(p_j(X)=(rX;r)_j\), including their value one at \(j=0\).
Keep the full original finite factors
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{k=0}^{N-1}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 C_{\beta,N}(Y,Z)&=\sum_{j=0}^{N-1}
                         Y^{-j}p_j(Y)p_j(Z)/P_j^{2+\beta},\\
 F_N(w,Y)&=N\operatorname{CT}_X
                         [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
 \mathscr D_{0,N}(w;y,z)&=F_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z).
\end{split}
 \tag{3}
\]
Here \(H_N\) is the original complete first-cap coefficient,
\(\operatorname{CT}_X\) takes the Laurent constant coefficient,
and \(d_N\) is the original polynomial of degree at most \(N-1\)
with \(d_N(r^b)=P_b^{-1}\). No row or Fourier forcing term
is removed in (3). The color \(w\) ranges over \([-2,2]\).

Let \(\Lambda_{123}(z)\) and \(\mathcal P_\beta^+(w,z)\)
be the affine bound and holomorphic action of the lower central
theorem. Their normalization at the actual output is
\[
 \Lambda_{123}(z_*)=
 \Re\mathcal P_\beta^+(-2,z_*)-\frac{\beta}{2}\Re g(z_*),
 \tag{4}
\]
where \(g\) is its original logarithmic primitive. These functions
are not redefined by the present extension.

Use exactly the first integration cycle of that theorem:
\[
\begin{split}
 \Gamma_a={}&[0,.1]\ \cup\
 \{x+ih_a(x-.1)/.12:.1\le x\le.22\}\\
 &{}\cup[.22+ih_a,.45+ih_a]\ \cup\
 [.45+ih_a,.5+ih_a]\ \cup\
 [.5+ih_a,.5]\ \cup\ [.5,1].
\end{split}
 \tag{5}
\]
Every piece has the increasing-coordinate orientation; the
vertical piece points upward. The endpoints agree on the
logarithmic cylinder. Holomorphy of the finite Laurent integrand
gives the exact identity
\[
 F_N(w,Y)=N\int_{\Gamma_a}
       U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da .
 \tag{6}
\]
The original factor \(N\) is included.

## 2. Bound for the entire first integral

**Theorem 1.** Uniformly on (1)--(2), for all real \(w\in[-2,2]\)
and all sufficiently large levels of both parities,
\[
 \boxed{\quad
 |\mathscr D_{0,N}(w;y,z)|\,|d_N(Z)|^{\beta/2}
 \le CN^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
 \quad}
 \tag{7}
\]
When \(\beta=0\), the outside factor is one, including at zeros
of \(d_N\). The conclusion concerns the entire \(F_N\).

*Proof.* The [complete initial and left-taper theorem](research_mixed_next_lower_right_shoulder_incoming_left.md)
bounds the integrals over the first two pieces of (5), with
their actual measure and every attached factor in (7).
Its bounds include both alternatives of the complete next
kernel: the ordinary affine bound and its explicit last-row
term. Their common finite deficit is \(10^{-11}\).

The [complete next-block theorem](research_mixed_next_lower_right_shoulder_next_block.md),
equation (8), bounds the full integrand on the central
piece \(P+ih_a\), with the same deficit. Integration over
this fixed piece multiplies the bound only by \(N|P|\).

Finally the [complete incoming right-tail theorem](research_mixed_next_lower_right_shoulder_incoming_right_tail.md)
bounds the integral over the last three pieces of (5), also
with deficit \(10^{-11}\). Its middle corner is used as the
combined oriented integral specified there. No bound for the
absolute integrals over its two original corner sides is
assumed. All following factors in (7) are independent of \(a\),
so that combined integral estimate applies directly to (6).

These pieces exhaust (5). Adding their bounds and absorbing
the finite sum of polynomial prefactors proves (7). Both
incident halves of the weight at \(Y\) give precisely the
single \(d_N(Y)\) in (3). \(\square\)

The source theorems retain all fixed real-color derivatives.
On sufficiently small fixed complex neighborhoods of complete
color and the actual output \(z_*\), they also retain the
normalized mixed derivatives. The outgoing halfweight is
removed only there, using the original nonzero packet.
The central estimate extends using its integer-power
holomorphic product and its strict gap. After choosing smaller
neighborhoods and absorbing polynomial costs, one may use
the common conservative loss
\[
                         \eta_{\rm sh}=10^{-13}.
 \tag{8}
\]
All paths, reference heights and integer cuts are held fixed
at their base values before outside parameters are varied.
Consequently, with \(\gamma_{\rm sh}=J_{\rm sh}+ih_y\),
\[
 \partial_w^j\partial_z^k
 \left[
  e^{-N\mathcal P_\beta^+(w,z)}
    N\int_{\gamma_{\rm sh}}\mathscr D_{0,N}(w;y,z)\,dy
 \right]=O_{j,k}(e^{-\eta_{\rm sh}N}).
 \tag{9}
\]
For an independent outgoing target in (2), (7) is instead
kept with its halfweight; no division at its possible zeros
is part of this assertion.

## 3. The original filter and denominator

Keep the original \(11/12\) filter, with its unchanged lower
cutoff, from Section 4 of the lower central theorem. Write
\[
\begin{split}
 F_N^{\rm mid}&=(I-\Pi)(F_N-R_N^{\rm node}),\\
 E_N&=F_N-F_N^{\rm mid},\\
 K_N(y)&=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}
                        {1-Y^N}.
\end{split}
 \tag{10}
\]
The symbols \(R_N^{\rm node}\) and \(\Pi\) retain their original
physical-node deletion and cardinal projection. In particular,
\(E_N\) is not a new contour remainder. The established bound is
\[
 \sup_{|Y|\le1}|E_N(w,Y)|\le CN^B e^{77N/50}.
 \tag{11}
\]

Section 2 of the right-tail theorem bounds any first-prefix
contribution with rate at most \(2383/1500\), after its full
remaining Fourier weight and next kernel are attached. It
proves this on (2) for both alternatives of the next kernel,
with a reserve greater than \(1/50\). Since
\(77/50<2383/1500\), it applies to (11). This uses the new
boundary-interval comparison, rather than extending a
comparison that was proved only on \(P\).

On \(\gamma_{\rm sh}\), uniformly in (1),
\[
 |Y^N|=e^{2\pi Nh_y}\le e^{-\pi N/500},
             \qquad |1-Y^N|\ge\frac12
 \tag{12}
\]
for all sufficiently large \(N\). There is thus no pole
on this lower interval. The exact difference is
\[
 K_N-N\mathscr D_{0,N}
 =N\,\frac{Y^NF_N-E_N}{1-Y^N}\,
                       d_N(Y)C_{\beta,N}(Y,Z).
 \tag{13}
\]
The \(F_N\) term is controlled by (7) and the additional
exponential factor in (12). The \(E_N\) term is controlled
by (11) and the just-verified comparison. Every original
factor in (13) remains present.

It follows that the filtered integral has the same normalized
bound as (9):
\[
 \boxed{\quad
 \partial_w^j\partial_z^k
 \left[
 e^{-N\mathcal P_\beta^+(w,z)}
        \int_{\gamma_{\rm sh}}K_N(y)\,dy
 \right]=O_{j,k}(e^{-\eta_{\rm sh}N}).
 \quad}
 \tag{14}
\]
The old correction polynomial has its complete real-color
bounds; the strict reserve allows the same fixed outside
neighborhoods and Cauchy derivative estimates. The denominator
and the integration path are fixed under these derivatives.

Adding (9) to the lower central asymptotic also shows that
the larger original integral
\[
 N\int_{[.22,.5]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
 =N^{-2-\beta/2}\mathcal A_\beta(w,z)
       e^{N\mathcal P_\beta^+(w,z)}
                  (1+O_{\rm hol}(N^{-1}))
 \tag{15}
\]
has exactly the original nonzero coefficient
\(\mathcal A_\beta\). This follows by addition of the two
specified integrals, not by replacing the full Fourier
coefficient with its central part.

## 4. The remaining signed contour

Let \(s>0\), \(H=1/100\), and the local geometric segment
be precisely those in
[upper seam-arc removal](research_mixed_next_top_seam_arc_removal.md).
Section 5 of the lower central theorem leaves, up to its
controlled error,
\[
\begin{split}
 \mathscr R_N^{\rm old}={}&
 \int_{[0,.22]+ih_y}K_N\,dy+
 \int_{[.45,1]+ih_y}K_N\,dy\\
 &-\int_{[s,.22]+iH}K_N\,dy
  -\int_{[.45,1-s]+iH}K_N\,dy .
\end{split}
 \tag{16}
\]
Splitting its second lower interval gives the exact identity
\[
 \mathscr R_N^{\rm old}
     =\int_{\gamma_{\rm sh}}K_N\,dy+\mathscr R_N^{\rm new},
 \tag{17}
\]
where
\[
\boxed{\begin{split}
 \mathscr R_N^{\rm new}={}&
 \int_{[0,.22]+ih_y}K_N\,dy+
 \int_{[.5,1]+ih_y}K_N\,dy\\
 &-\int_{[s,.22]+iH}K_N\,dy
  -\int_{[.45,1-s]+iH}K_N\,dy .
\end{split}}
 \tag{18}
\]
Only a positive lower interval has been removed. Both upper
intervals and their minus signs are unchanged. No new contour
deformation is made in (17), and the original cyclic identity
has already canceled its vertical sides exactly.

For an explicit combined error, let \(\eta_\rho>0\) be the
loss in equation (15) of the lower central theorem, with its
fixed local segment, and let \(\Delta=59/440000\) be the
upper seam-arc constant. Set
\[
 \eta=\frac12\min\{\eta_\rho,\Delta/64,\eta_{\rm sh}\}>0.
 \tag{19}
\]
Combining its lower central estimate, the upper seam-arc
identity and (14)--(17) gives
\[
\partial_w^j\partial_z^k\left[
 e^{-N\mathcal P_\beta^+(w,z)}
 \{\mathcal T_\beta[F_N]-I_{\rm geom,N}
                         -\mathscr R_N^{\rm new}\}
 \right]=O_{j,k}(e^{-\eta N}).
 \tag{20}
\]
Here \(\mathcal T_\beta\) is the original sum of the constant
and \(N\)-th Fourier coefficients, with their original
factor \(N\), and \(I_{\rm geom,N}\) is the original local
geometric integral. The minimum in (19) is necessary:
the older larger error constant cannot be carried unchanged
through the new estimates.

No bound at the required rate has yet been proved for the signed sum (18).
This theorem removes the complete interval
\([.45,.5]+ih_y\); it does not remove either whole Fourier
coefficient or prove the next-transfer asymptotic. Stability
under arbitrary fixed short fillings, and hence the stated
finite-exceptions goal, remain open.
