# Uniform large-color matching with the canonical finite cutoff

Private written proof, 18 November 2026.

The exact fixed-color comparison in [B] has two endpoint amplitudes.
Here their dependence on the color is bounded using the same canonical
Borel germ and the actual finite-color estimate [A]. This proves an
exponentially accurate comparison uniformly when the color grows like
the inverse quantum parameter, on a small initial meridian arc.
No infinite Laplace contour or uniqueness of sectorial sums is used.

## 1. Source and uniform assertion

Fix the original one-component braid source and its reduced,
zero-framed color polynomials \(C_L(q)\), \(L\ge1\), as in [A].
Use
\[
 h=\log Q,\qquad q=e^{h/2},\qquad u=\log Y.
 \tag{1}
\]
Let the canonical source and its ordinary Borel germ be
\[
 \widehat{\mathscr W}(h,e^u)=\sum_{j\ge0}h^j a_j(u),\qquad
 b(u,\xi)=\sum_{j\ge0}a_j(u)\frac{\xi^j}{j!}.
 \tag{2}
\]
The source in [B] is jointly holomorphic near \(u=\xi=0\).
Its exact formal color restriction is
\[
       \widehat{\mathscr W}(h,e^{Lh})=C_L(e^{h/2}).
 \tag{3}
\]
All source conventions, including the original cut and pivot, are
retained. No Alexander-root or transverse-node hypothesis is needed
for this neighborhood of \(Y=1\).

Choose \(d>0\), \(R_0>0\), and \(M>0\) so that \(b\) is holomorphic
on a neighborhood of
\[
             |u|\le 2d,\qquad |\xi|\le R_0,
 \qquad |b(u,\xi)|\le M .
 \tag{4}
\]
Shrink these constants when necessary below. For any fixed
\(0<|R|\le R_0\), use the straight Borel path from zero to \(R\) and
define the actual canonical cutoff
\[
 U_R(h,e^u)=\frac1h\int_0^R e^{-\xi/h}b(u,\xi)\,d\xi,
 \qquad h\ne0.
 \tag{5}
\]
The path and endpoint are independent of \(u,h,L\).

**Theorem.** For each \(0<\sigma<\pi/2\), there are \(u_1,C>0\),
independent of \(L,h\), such that
\[
 \left|U_R(h,e^{Lh})-C_L(e^{h/2})\right|
 \le C\exp\!\left(-\frac{\sin\sigma}{2}
                         \frac{|R|}{|h|}\right)
 \tag{6}
\]
whenever
\[
 L\ge1,\qquad 0<|Lh|\le u_1,\qquad
 |\arg h-\arg R|\le\frac\pi2-\sigma .
 \tag{7}
\]
The angular condition means the corresponding inequality for the
chosen directions, without a branch ambiguity.
The constants may be chosen uniformly for the straight endpoints in
(4); in particular they are valid for each fixed nonzero \(R\).
The range includes \(L=O(|h|^{-1})\). It is a small logarithmic
meridian disk, and does not include \(Lh=2\pi i\).

## 2. The actual shift amplitude, uniformly in its length

Let \(I\) be the primitive in \(\xi\), along the same straight path.
For a real parameter \(s\ge0\), the actual semigroup of [B] is
\[
 c_s(u,\xi)=e^{sI\partial_u}b(u,\xi)
          =\sum_{n\ge0}\frac{s^n}{n!}I^n\partial_u^n b(u,\xi).
 \tag{8}
\]
For \(|u|\le d\), Cauchy's formula in (4), and the literal repeated
primitive, give
\[
 |\partial_u^n b|\le M n!d^{-n},\qquad
 |I^n f|\le\frac{|R|^n}{n!}\sup|f|.
 \tag{9}
\]
The latter estimate holds also at every intermediate point of the
straight segment. Consequently, with \(t=s|R|/d\),
\[
 |c_s|\le M e^t,\qquad
 |\partial_u I c_s|\le \frac{M|R|}{d}e^t .
 \tag{10}
\]
For the second estimate, keep the extra primitive and derivative
together: its \(n\)-th summand is
\(s^n I^{n+1}\partial_u^{n+1}b/n!\).
The two \((n+1)!\) factors from (9) cancel. Thus (10) has no
additional polynomial factor in \(s\).
These absolutely convergent series justify the differentiations
and the transport equation for every finite \(s\), with the displayed
estimates retaining its full size.

For \(|Lh|\le d\), every point \(u=(L-s)h\), \(0\le s\le L\),
lies in the same inner disk. The exact shift endpoint amplitude is
\[
 K_L(h)=\int_0^L
             (\partial_u I c_s)((L-s)h,R)\,ds .
 \tag{11}
\]
Integrating (10) gives the uniform bound
\[
          |K_L(h)|\le M\bigl(e^{L|R|/d}-1\bigr).
 \tag{12}
\]
In particular an unbounded prefactor \(L\) is not hidden in (12).

The exact identity underlying (11) remains valid on this full
color-dependent disk, not just in an unspecified fixed-color germ.
Indeed integration by parts in the finite path gives, for
\(v_s=\mathcal L_R c_s\),
\[
 \partial_s v_s=h\partial_u v_s
                   -e^{-R/h}\partial_u I c_s(u,R).
 \tag{13}
\]
Integrate along \(u=(L-s)h\). Since \(v_0=U_R\), one obtains
\[
        U_R(h,e^{Lh})
             =\mathcal L_R c_L(0,\cdot)+e^{-R/h}K_L(h).
 \tag{14}
\]
All paths in this calculation stay inside the fixed logarithmic
disk. This checks explicitly the required uniform domain of the
original shift comparison.

## 3. The scalar endpoint amplitude from the original color bound

The complete finite-color estimate [A] supplies \(u_0,M_0>0\) with
\[
 f_L(u):=C_L(e^{u/(2L)}),\qquad
           \sup_{L\ge1,\ |u|\le u_0}|f_L(u)|\le M_0.
 \tag{15}
\]
For example its summable finite-sector bound proves (15) directly;
its uniform limit on a slightly larger disk also suffices, with
the finitely many small colors included. The color-one polynomial
is \(1\). This is a bound for the original finite-color source,
not for an independently chosen formal solution.

Write \(C_L(e^{h/2})=\sum_{j\ge0}c_{L,j}h^j\).
Cauchy's formula applied to (15), with \(u=Lh\), gives
\[
                    |c_{L,j}|\le M_0(L/u_0)^j.
 \tag{16}
\]
The scalar endpoint amplitude in [B] is therefore the convergent
series
\[
 A_L(h,R)=\sum_{k,m\ge0}c_{L,k+m}h^k\frac{R^m}{m!},
 \qquad
 |A_L(h,R)|
 \le \frac{M_0e^{L|R|/u_0}}{1-L|h|/u_0}
 \quad(L|h|<u_0).
 \tag{17}
\]

For completeness, the source identification in this formula is exact.
By (3), the Borel transform of the formal substitution is
\[
                 c_L(0,\xi)
                   =\mathcal B_h[C_L(e^{h/2})](\xi).
 \tag{18}
\]
Both sides are analytic near zero, and the right side is entire
in \(\xi\), because \(C_L\) is a finite Laurent polynomial in \(q\).
Equation (18) consequently holds on the selected short segment.
Termwise integration, justified by (16), gives
\[
          \mathcal L_R c_L(0,\cdot)
                         =C_L(e^{h/2})-e^{-R/h}A_L(h,R).
 \tag{19}
\]
Combining (14) and (19) retains both endpoint contributions:
\[
 U_R(h,e^{Lh})-C_L(e^{h/2})
                  =e^{-R/h}\{K_L(h)-A_L(h,R)\}.
 \tag{20}
\]
For each \(L\), this is [B]'s actual comparison. Equations
(12) and (17) now bound it uniformly as the color grows.

## 4. Exponential competition on the initial arc

Put
\[
                 A_*=\max(d^{-1},u_0^{-1}).
 \tag{21}
\]
Whenever \(L|h|\le\min(d,u_0/2)\), (12) and (17) give
\[
 |K_L(h)-A_L(h,R)|\le C e^{A_*L|R|}.
 \tag{22}
\]
Choose
\[
 0<u_1\le\min\left(d,\frac{u_0}{2},
                         \frac{\sin\sigma}{2A_*}\right).
 \tag{23}
\]
The facing-sector condition in (7) gives
\[
 \Re(R/h)\ge\sin\sigma\,\frac{|R|}{|h|},\qquad
 A_*L|R|\le A_*u_1\,\frac{|R|}{|h|}.
 \tag{24}
\]
Substitution in the exact identity (20) proves (6).
The estimate is absolute and uniform, including sequences for which
\(L\to\infty\) and \(Lh\) remains in a fixed small part of the arc.
It does not rely on keeping \(L\) fixed before taking \(h\to0\).

This matches the actual finite-color values to a specified canonical
finite cutoff on the initial meridian domain. The exponentially small
endpoint discrepancy remains present. The theorem neither identifies
an infinite Borel sum nor continues the comparison to an Alexander
root, to a nonabelian component, or to \(Lh=2\pi i\).
No physical complete-root scalar lower bound follows from this local
comparison alone.

## 5. Complete proof sources

| Label | Complete source | SHA256 |
|---|---|---|
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |
| A | notes/research_finite_color_small_meridian_analytic_anchor.md | 946a0495603a1a0fc92965c8e70a99c403c4cfb22952cd6838cf3beb20c2f0ba |

B supplies the canonical germ, exact shift semigroup and original
fixed-color endpoint identity. A supplies the uniform bound on the
original finite-color polynomials. Their quantitative combination,
including the common logarithmic domain for growing \(L\), is proved
above. No external proof, mathematical program, test or build is used.
Frozen notes and public manuscripts are unchanged.
