# A coherent-private half-face criterion for the physical middle sector

Research reduction, 7 November 2026. Keep the transform index real
and deform only the complete private source inside the terminal
factor. The physical incoming interval \([1/2,5/6]\) then has a
shape-dependent upper envelope which decreases towards its far
endpoint. The entire interval reduces to one explicit half-face
comparison involving five private-current profiles. That comparison
is not proved here. No numerical evaluation is used.

## 1. Original finite source and the physical first-cap envelope

Use \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), \(p_j(X)=(rX;r)_j\),
and the exact source of
[the ordinary pair](research_mixed_three_four_ordinary_pair_target.md):
\[
\begin{split}
 V_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i),\\
 U_{1,N}(w,r^i)&=\sum_{j=0}^{N-1-i}
       \frac{H_N(w,r^{-j})P_{i+j}}{P_iP_j^2},\\
 Z_{34,N}&=\kappa_N^3N\sum_{b=0}^{N-1}
                  U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b).
\end{split}
 \tag{1}
\]
Every \(H_N\) is its whole endpoint polynomial. At \(X=r^b\),
the first sum terminates at \(i=N-1-b\). These two support
statements are exact physical zeros, not off-grid deletions.

Put \(J(t)=\int_0^t\log(2\sin\pi s)\,ds\), with its continuous
endpoint values, and set
\[
\begin{split}
 Q(v,u)&=-2J(1/2-u)-4J(u)-J(v-u)+2J(v),\\
 \overline Q(v)&=\max_{0\le u\le v}Q(v,u),\\
 W(v,t)&=J(v)-J(v-t)-2J(t).
\end{split}
 \tag{2}
\]
For complex arguments below, \(J\) denotes its original holomorphic
continuation on \(0<\Re z<1\); no logarithmic lift is changed.
Here \(v=1-b/N\in[1/6,1/2]\). The
[physical far-half proof](research_mixed_three_four_physical_far_half.md),
Section 2, proves that \(\overline Q\) is strictly increasing on
\((0,1/2]\), that \(\overline Q(1/2)<41/40\), and that the
whole physical \(U_0\) has upper rate \(\overline Q(v)\).
The exact outer coefficient of (1) has rate \(W(v,t)\),
where \(t=i/N\le v-1/N\). Its factor \(r^{-bi}\) has modulus one.
All these finite upper estimates are zero safe and have uniform
polynomial prefactors and arbitrarily small color tolerances.
The all-real-color extension of the first-cap estimate follows
directly from its terminating formula (7): every Newton index obeys
\(u\le v\le1/2\), where the
[zero-safe Newton theorem](research_mixed_newton_color_tubes.md)
gives \(V_\theta(u)\le V_0(u)\). Thus the same
\(\overline Q(v)\) bounds every \(w_L\in[-2,2]\).
Markov's inequality on that whole real color interval supplies
fixed ordinary derivatives before any strict gap is allocated.

Remove the full transform rows \(i/N\le\delta\) first, for a
sufficiently small fixed \(\delta<1/10\) supplied by
[the global transform-end theorem](research_mixed_three_four_global_transform_ends.md).
Their product with the complete first cap is already bounded by
\(CN^A e^{N(M-1/20)}\), where \(M\) is the unchanged ordinary
pair action. The other true transform end is zero on the present
physical incoming sector. This deletion is made before restricting
any private or Newton sum.

## 2. The full private contour for every remaining real transform row

Retain the original cap phase
\[
 \Psi_1(e,t)=S(e)+J(e+t)-J(t)-i\pi et-g(e),\qquad
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),
 \tag{3}
\]
and \(E_c=[.27,.49]+i[-.055,.04]\). Choose any fixed
private main height \(h_e\in(-.055,.04)\). Its five profiles are
\[
\begin{split}
 A_0(t)&=\max_{.27\le u\le.49}\Re\Psi_1(u+ih_e,t),\\
 A_L(t)&=\Re\Psi_1(.27,t),\qquad
 A_R(t)=\Re\Psi_1(.49,t),\\
 A_-(t)&=\max_{.27\le u\le.49}\Re\Psi_1(u-.055i,t)-.11\pi,\\
 A_+(t)&=\max_{.27\le u\le.49}\Re\Psi_1(u+.04i,t)-.08\pi,\\
 A(t;h_e)&=\max\{A_0(t),A_L(t),A_R(t),A_-(t),A_+(t)\}.
\end{split}
 \tag{4}
\]
In particular both cuts remain real.

**Lemma 1.** For physical \(t=i/N\in[\delta,1/2]\), the entire
finite \(U_{1,N}(w,r^i)\) has upper rate \(A(t;h_e)\), with one
arbitrarily small tolerance. The statement holds for both parities,
all real ordinary colors, a sufficiently small complex color disk
about \(-2\), and every fixed ordinary derivative.

*Proof of the central contour.* The literal interpolant is
\[
 D_N(e)^{-1}C_N(e,w)
       \frac{\widehat P_N(N(e+t))}
            {\widehat P_N(Nt)\widehat P_N(Ne)}.
 \tag{5}
\]
All its factorial arguments are regular on a fixed neighborhood
of \(E_c\times[\delta,1/2]\). The coefficient \(C_N\) remains
whole and has its original upper rate \(\Re S(e)\).
The exact curvature in
[the complex-private theorem](research_mixed_cap_early_taper_complex_profiles.md),
Lemma 1, gives \(-\Re S''(e)>\pi C(e)\), where
\(C(e)=\Re\cot\pi e>0\).

At fixed \(\Im e\), \(C(e+t)<C(e)\) if
\(\Re(e+t)<1/2\): on \(1/4<\Re e<1/2\), its real-coordinate
derivative has numerator
\(2\pi[\cos(2\pi\Re e)\cosh(2\pi\Im e)-1]<0\).
If \(\Re(e+t)\ge1/2\), then \(C(e+t)\le0\), since
\(\Re(e+t)\le.99\). Therefore
\[
 -\Re\Psi_{1,ee}
       =-\Re S''(e)+\pi C(e)-\pi C(e+t)>0.
 \tag{6}
\]
This is uniform on the stated compact product. The original
one-index residue formula retains the zero-mode factor \(+N\),
the main segment, both joins, both horizontal aliases and all
vertical alias sides. Vertical convexity reduces their rates to
exactly (4), with the original penalties. The real-color endpoint
bound, or its fixed complex-color version, applies before any
modulus is taken. No transform contour is introduced.

*Proof for all physical private tails.* The upper rate of a physical
private row is
\[
 R(e,t)=\lambda(e)+J(e+t)-J(t)-J(e),
        \qquad \lambda(e)=\Re S(e),\quad 0\le e\le1-t.
 \tag{7}
\]
For \(0<e<1/2\), \(\lambda''<0\), and
\[
 R_{ee}=\lambda''(e)+\pi\cot\pi(e+t)-\pi\cot\pi e<0.
 \tag{8}
\]
At the lower cut, the old scalar \(\lambda'(.27)>27/50\)
and the minimum of sine on \([.27,.77]\) imply
\[
 R_e(.27,t)\ge\lambda'(.27)+\log\cot(.27\pi)>\frac1{25}.
 \tag{9}
\]
Indeed \(\cot(.27\pi)>\tan(\pi/5)>2/3\), using
\(\tan z>z+z^3/3\) and \(\pi>3\); and
\(\log(2/3)>-1/2\), since \(e^{1/2}>3/2\).
Equation (8) transports the full lower private tail to .27.

On \([.49,.5]\), the original bounds
\(\lambda'<-3/5\), \(J'>3/5\) and \(\log2<7/10\) give
\(R_e<-1/2\). For \(e\ge1/2\), the exact endpoint identity
\(\lambda'-J'\le-\log4\) gives \(R_e\le-\log2\), up to
the physical wall \(e+t=1\). Thus the upper tail reduces to
.49. These are the bounds used in
[the early real-row proof](research_mixed_cap_early_taper_real_rows.md),
Section 3, with the transform target real.

To justify uniformity at the genuine private ends, fix \(\delta\)
before taking any contour. The support in (1) has
\(j/N\le1-\delta-1/N\). The whole physical coefficient bound
in [terminal real-color decay](research_mixed_terminal_real_color_decay.md),
equation (8), consequently covers every retained private row,
including \(j=0\). Its near-complete-color counterpart follows
from the same zero-safe endpoint argument. The uniform physical
factorial bounds give (7) through its endpoints with a prescribed
tolerance. At the lower endpoint \(R(0,t)=0\), and (8)--(9)
place it below the lower cut; the upper derivative bounds extend
to the support endpoint by integration and continuity. No
unavailable off-grid endpoint packet is used.

Every physical private row is therefore included in (4).
Half-grid cuts move its regular anchor rates by \(O(1/N)\).
Polynomial counts, fixed ordinary derivatives, and all other
finite-symbol errors can be absorbed in one tolerance.
\(\square\)

## 3. The small remaining transform rows reduce to \(t=1/10\)

Let \(a=x\) be real, \(1/2\le x\le5/6\).
At a real transform index \(0<t\le1/10\), every point of the
private contour obeys the exact original logarithmic identity
\[
 e^{\partial_t\Re\Phi(a;t,e)}
 =\frac{2\sin\pi(x+t)\,
          |1-e^{-2\pi i(e+t)}|}
         {(2\sin\pi t)^3}>\frac85.
 \tag{10}
\]
Here \(\Phi\) is the terminal phase in
[the height-transport note](research_mixed_three_four_far_half_height_transport.md),
equation (1), and its incoming chirp is retained.

For completeness, \(x+t\in(1/2,14/15]\), so the first factor
is at least \(2\sin(\pi/15)>2/5\). One elementary witness is
\(\pi>31/10\) and
\(\sin(31/150)>31/150-(31/150)^3/6>1/5\).
The real part of \(e+t\) lies in \([.27,.59]\), where its
doubled cosine is negative; its modulus factor is therefore
greater than one at every permitted private height. Finally
\[
 2\sin(\pi/10)=\frac{\sqrt5-1}{2}<\frac58,\qquad
                    (5/8)^3<1/4.
 \tag{11}
\]
This proves (10) without evaluating a source or a phase.

The identity of rates is
\[
             \Re\Phi(1-v;t,e)=\Re\Psi_1(e,t)+W(v,t).
 \tag{12}
\]
Every private penalty in (4) is independent of \(t\). Integrate
(10) for each contour point and then take the appropriate
maximum. Hence all remaining physical rows
\(\delta<t<1/10\) reduce to \(t=1/10\).
The continuous comparison target need not be a lattice row.
All whole-private currents have already been retained in Lemma 1.

## 4. A monotone complete-sector envelope and its exact remaining test

Define
\[
 \mathcal E(v;h_e)=\overline Q(v)+
     \max_{1/10\le t\le v}\{A(t;h_e)+W(v,t)\},
                     \qquad 1/6\le v\le1/2.
 \tag{13}
\]
For every tolerance \(\tau>0\), the complete physical product has
the finite upper bound
\[
\begin{split}
 &|U_{0,N}(w_L,r^b)V_{1,N}(w_R,r^b)|\\
 &\quad\le C_\tau N^{B_\tau}
   \left[e^{N(M-1/20)}
          +e^{N\{\mathcal E(1-b/N;h_e)+\tau\}}\right],
       \qquad \frac12\le\frac bN\le\frac56 .
\end{split}
 \tag{14}
\]
The two terms respectively retain the full true-transform-end
deletion and all remaining transform rows. The proof has taken
absolute values only after each complete private cap has been
bounded. No inner Newton sub-sum or coherent terminal half-face
value replaces that private cap.

There is an exact incoming monotonicity, independent of the
chosen private height. For \(0<t<v\le1/2\),
\[
 \partial_vW
  =\log\frac{\sin\pi v}{\sin\pi(v-t)}
  \ge-\log\cos\pi t\ge\frac{\pi^2t^2}{2}.
 \tag{15}
\]
The first inequality follows by writing the denominator ratio
as \(\cos\pi t-\cot\pi v\sin\pi t\). The last is
\(-\log\cos z\ge z^2/2\). The primitive is continuous at
\(t=v\), so integration and maxima preserve the inequalities.
Together with the strict increase of \(\overline Q\), this
shows that \(\mathcal E(v;h_e)\) is strictly increasing and,
more precisely,
\[
 \mathcal E(v;h_e)
 \le\mathcal E(1/2;h_e)
       -[\overline Q(1/2)-\overline Q(v)]
       -(1/2-v)\frac{\pi^2}{200}.
 \tag{16}
\]

Thus a sufficient remaining comparison for the entire physical
middle sector is
\[
 \boxed{\quad
 \overline Q(1/2)+
 \max_{1/10\le t\le1/2}
  \{A(t;h_e)-J(1/2-t)-2J(t)\}<M .
 \quad}
 \tag{17}
\]
All five private profiles are part of \(A\). Their main height
may be chosen once anywhere strictly inside its original range.
If (17) holds with a fixed reserve, (14)--(16), the original
\(\kappa_N^3N\) in (1), and polynomial row counts give a strict
finite gap for the complete middle root sum. The finite estimates
hold with independent near-complete ordinary colors, or with both
colors real, and every fixed ordinary derivative, after keeping
one common tolerance.

No sign of (17) is asserted. In particular neither the completed
height-\(c\) terminal plane nor the value of the signed terminal
polynomial at the half point proves this real-transform upper
envelope comparison. A failed comparison for this envelope would
not prove failure of the source; it would call for retaining
transform cancellation as well. Finally, even a successful
physical-sector deletion is not an estimate of a continuous arc:
all aliases and joins of any subsequent partial incoming
root-sum contour remain separate.

This criterion is distinct from Proposition 2 of
[the reversed-cap assembly](research_mixed_reversed_cap_assembly.md).
That obstruction concerns a triangle bound over both real private
and real transform indices at the actual complex incoming reference.
Here the private index retains its complete deformed contour, while
the incoming comparison is the real physical half face. The old
obstruction neither proves nor disproves (17), and neither argument
establishes the half-face sign.
