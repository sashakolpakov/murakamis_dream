# Critical localization for every open word with ordinary endpoints

Research proof, 5 November 2026. Four finite endpoint maps and two
one-vertex disks establish a unique original critical point for every
nonempty open word. This is a critical-geometry theorem; the full
finite-source contour theorem remains a separate requirement. Frozen
upstream artifacts are unchanged.

## 1. The original endpoint equations

Fix a nonempty word \(3+\epsilon_1,\ldots,3+\epsilon_m\).
Use the original action \(\mathcal F_m\), rectangles \(E,U,Q\), and
strict Hessian bound from
[the open-word Hessian lemma](research_mixed_open_word_hessian.md).
The ordinary boundary variables \(u_L,u_R\) are part of that action.
For a private endpoint \(e\), the selected complete-end coordinate is
\[
 u_c(e)=\pi^{-1}\arctan\frac{i+\sqrt{1-2e^{2\pi i e}}}{2},
 \qquad
 S(e)=B(e,u_c(e))+i\pi e u_c(e).                         \tag{1}
\]
The square root and arctangent have the original continuations from
the positive real sine chamber. In particular
\[
 S'(e)=-J'(e-u_c(e))+i\pi u_c(e).                         \tag{2}
\]
The original full boundary sum, including its endpoint chirps, gives
these derivatives; replacing an ordinary endpoint by a fixed
holomorphic amplitude would omit (2).

For an interior leg the eliminated critical equations are
\[
\begin{split}
0={}&J'(s_j+t_j)+J'(t_{j-1}+s_j)-(2+\epsilon_j)J'(s_j)
 +i\pi[t_{j-1}-t_j+\epsilon_j(s_j-1/2)],\\
0={}&J'(s_j+t_j)+J'(t_j+s_{j+1})-(2+\epsilon_j)J'(t_j)
 +i\pi[s_{j+1}-s_j+\epsilon_j(t_j-1/2)].                 \tag{3}
\end{split}
\]
The first equation applies for \(j>1\), and the second for \(j<m\). The private
left equation is
\[
 S'(s_1)+J'(s_1+t_1)-\epsilon_1J'(s_1)
       +i\pi[-t_1+\epsilon_1(s_1-1/2)]=0,                \tag{4}
\]
and the private right equation is its reversal. All logarithms retain
their zero lift. The finite \(N-1\) correction and fixed ordinary
derivative orders belong to amplitudes; changing the ordinary color
itself changes the leading endpoint action.

## 2. Four endpoint maps

Use the original cyclic disks
\[
 D_3=\{|z-(.35-.01i)|\le.09\},\qquad
 D_4=\{|z-(.30-.052i)|\le.064\}.                         \tag{5}
\]
Both are strictly inside \(Q\). Given the external attached leg
\(b\in D_{3+\delta}\), the endpoint vertex of type
\(3+\epsilon\) solves for its private leg \(e\), attached leg
\(t\), and auxiliary coordinate \(u\):
\[
\begin{split}
 f_e={}&-J'(e-u)+J'(e+t)-\epsilon J'(e)
          +i\pi[u-t+\epsilon(e-1/2)],\\
 f_t={}&J'(e+t)+J'(t+b)-(2+\epsilon)J'(t)
          +i\pi[b-e+\epsilon(t-1/2)],\\
 f_u={}&2\operatorname{Log}\cos\pi u
       +\operatorname{Log}\sin\pi(e-u)
       -3\operatorname{Log}\sin\pi u+i\pi e.             \tag{6}
\end{split}
\]
Reversing an open word swaps its two endpoint constructions without
changing (6). Thus there are four typed disk domains, rather than
word-length-dependent families.

**Lemma 1.** Equation (6) has for every external input
exactly one zero in \(E\times Q\times U\), and it satisfies
\[
                e\in\operatorname{int}E,\qquad
 t\in\operatorname{int}D_{3+\epsilon},\qquad
                u\in\operatorname{int}U.                \tag{7}
\]
It is holomorphic on a neighborhood of the closed input disk, and
\(u=u_c(e)\) on the original endpoint branch.

Here is the complete outward test. Normalize the external disk to the
unit disk, cover its enclosing square by binary rational rectangles,
and exclude a rectangle only if its minimum squared radius is
strictly greater than one. A retained leaf supplies rational complex
\(z_0=(e_0,t_0,u_0)\), rational complex matrix \(Y\), and rational
\(r>0\). For the whole parameter rectangle and the whole product of
complex radius-\(r\) disks about \(z_0\), verify
\[
 \det Y\ne0,\qquad
 |(Yf(z_0,b))_i|+
 r\sum_j|(I-Yf_z(z,b))_{ij}|<r\quad(1\le i\le3).        \tag{8}
\]
The derivative is enclosed on the larger Cartesian squares. The same
squares stay in \(E,Q,U\), while the attached image disk separately
satisfies \(|t_0-\operatorname{center}D|+r<\operatorname{radius}D\).
Banach's theorem gives an actual original-log zero at every input.
The Hessian lemma gives uniqueness throughout the larger convex
product, hence agreement on overlaps and holomorphic continuation.

The checker also evaluates (1) on every private-leg enclosure. It
verifies \(0<\Re u_c<1/2\), \(0<\Re(e-u_c)<1/2\), and that its
original \(f_u\) residual has modulus less than \(\pi\). The exact
complete-end quadratic identity makes this residual an integer
multiple of \(2\pi i\), hence zero. Scalar strict accretivity on
that sine chamber identifies it with the coordinate in (7).

## 3. All lengths, including one and two

For \(m\ge2\), consider the compact convex product with private
legs in \(E\), endpoint auxiliaries in \(U\), and all other legs
in their typed disks (5). At each internal vertex update its two
legs with the already certified cyclic local map, using the old
external legs. At either endpoint update all three coordinates with
(6), again using its old external leg. These coordinate groups are
disjoint. If (7) is certified, this is a continuous self-map of that
product. Brouwer's theorem supplies a fixed point. At the fixed point
the equations are precisely all original open gradient equations,
not a periodic identification or a modified boundary equation.

At length two there are no internal vertices. The two endpoint maps
use one another's old attached legs; at a fixed point their shared
edge has its literal two distinct leg coordinates. This construction
requires no extra length-two domain. The uniform Hessian bound makes
the resulting critical point unique in the larger product
\(\mathcal D_m\).

Length one has two private legs and two auxiliary coordinates. The
action is invariant under their exchange. For each of its two types
the checker supplies a separate two-variable original-log disk with
\(s_1=t_1=e\), \(u_L=u_R=u\), solving
\[
\begin{split}
0={}&-J'(e-u)+J'(2e)-\epsilon J'(e)
                  +i\pi[u-e+\epsilon(e-1/2)],\\
0={}&2\operatorname{Log}\cos\pi u
 +\operatorname{Log}\sin\pi(e-u)-3\operatorname{Log}\sin\pi u
 +i\pi e.                                                \tag{9}
\end{split}
\]
This is an actual zero of all four original equations by symmetry.
Its original-log Newton test is (8) in two variables, and its boxes
lie in \(E\times U\). Full four-variable injectivity then gives
uniqueness, including against nonsymmetric candidate roots.

**Theorem 2.** Every nonempty open word has exactly one critical point
in the common product \(\mathcal D_m\). Its private legs and auxiliary
coordinates satisfy (7), and every internal leg is in its original
typed disk (5). The critical point is simple and its negative real
Hessian is greater than \(6\pi/49\).

The four endpoint covers and both one-vertex disks below complete
the existence arguments above; the Hessian lemma supplies uniqueness.
This does not prove the finite endpoint coefficient's
asymptotic on all of the complex endpoint image, global contour
dominance, the original open-word nonzero coefficient, or an enlarged
knot-family theorem. The source neighborhood in the existing complete
boundary theorem has unspecified width; the present root localization
does not enlarge it.

## 4. Reproduction

Floating roots and inverses propose rational witnesses only. Saved
mode checks every exact tree, exclusion, Newton witness, branch test,
and file binding without root proposals. No parameter box can be
silently omitted, and the two one-vertex cases are compulsory.

The complete cover has 5,258 accepted cells and 233 excluded rectangles
(10,978 total tree nodes). The four accepted-cell counts, in own/neighbor
type order \((3,3),(3,4),(4,3),(4,4)\), are respectively
1,645, 1,702, 1,002, and 909. Both one-vertex disks pass separately.
Author and saved-replay records determine the current verification
status and bind the exact proof, scripts, and inherited inputs.

```sh
python3 experiments/certify_mixed_open_word_critical_localization.py --precision 256
python3 experiments/certify_mixed_open_word_critical_localization.py --precision 320 --input repro/results/research-mixed-open-word-critical-localization.json --output repro/results/research-mixed-open-word-critical-localization-replay.json
```
