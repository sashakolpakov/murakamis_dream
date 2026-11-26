# A complete boundary asymptotic for the mixed two-crossing tangle

This note proves the asymptotic of the original boundary polynomial
\(T(R^{-2}T(R^2))\), including all first normals, both level parities,
every factorial index, and every term of its exact contour identity.
Its leading coefficient is nonzero on a fixed complex disk. The whole
real boundary period has a strict angular loss, which extends to a
fixed complex strip.

The result is analytic. Its critical action and original primitive
periods are identified with the marked hyperbolic complement in
[the separate collar representation proof](research_mixed_word_collar_representation.md).
That proof uses a positive triangulation, the original diagram's
group presentation and exact peripheral transport.

## 1. The original source and the theorem

Use the full quotient
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\), the original crossing
\(R\), and the Newton reversal \(T\). Set
\[
 Z_N(u)=\operatorname{can}\bigl(T(R^{-2}T(R^2))\bigr)(-2\cos u).
                                                               \tag{1}
\]
Its exact coefficients and complete normalization are given in
[the mixed-source calculation](research_mixed_two_crossing_horizontal_dominance.md).
In particular, it is the full original polynomial of degree at most
\(N-1\) in \(-2\cos u\).

Define
\[
 W(x,y;u)=J(x+y)-3J(x)-2J(y)+b(y,u)
                         +i\pi(xy-y^2/2-y/2),          \tag{2}
\]
where the logarithmic primitives and their branches are exactly
those in that calculation. Let \(X\) be the upper root of
\(X^3+2X^2+1=0\), put \(Y=1+2X+2X^2\), and set
\[
       x_*=\frac{\log X}{2\pi i},\qquad
       y_*=\frac{\log Y}{2\pi i}.
\]
The literal, unexponentiated derivatives of (2) vanish at this point
when \(u=0\). Its negative horizontal real Hessian is positive
definite. Let \((x(u),y(u))\) be its holomorphic critical extension,
and define
\[
 S(u)=W(x(u),y(u);u),\qquad M=\Re S(0).
\]
Use
\[
 a(x,y)=\frac{e^{i\pi y/2}}8
        \frac{\sqrt{\sin\pi(x+y)}}
             {(\sin\pi x)^{3/2}(\sin\pi y)^2},
\]
with its continuation from the positive real factorial triangle,
and set
\[
 A(u)=\frac{2\pi a(x(u),y(u))}
              {\sqrt{\det[-W''(x(u),y(u);u)]}}.         \tag{3}
\]
Here \(W''\) is the Hessian in \(x,y\). The denominator is the
Gaussian square root fixed by its positive definite real quadratic
part at zero.

**Theorem 1.** There is a fixed disk \(|u|\le r\) on which \(A\)
is holomorphic and nonzero, and, through every integer level,
\[
 \boxed{\displaystyle
                 Z_N(u)=A(u)e^{NS(u)}(1+O(N^{-1})).}     \tag{4}
\]
The normalized error is holomorphic, and each of its fixed
derivatives is \(O(N^{-1})\) on smaller disks. There are positive
constants \(c,b\), a finite \(B\), and fixed polynomial prefactors
such that
\[
 |Z_N(x+iy)|\le C N^d
      \exp N\{M-c(1-\cos x)+B y^2\},\qquad
                      |x|\le\pi,\quad |y|\le b.        \tag{5}
\]
The critical action is even, and its boundary curvature is
\[
 S''(0)=-\frac{\tan(\pi y_*)}{2\pi},
                         \qquad-\Re S''(0)>0.          \tag{6}
\]
In particular, \(Z_N(0)\ne0\) for all sufficiently large \(N\), and
\[
       \lim_{N\to\infty}\frac{2\pi}{N}\log|Z_N(0)|=2\pi M.
                                                               \tag{7}
\]
The sign-reversed source \(T(R^2T(R^{-2}))\) has the holomorphic
germs \(A_-(u)=\overline{A(\overline u)}\) and
\(S_-(u)=\overline{S(\overline u)}\), and the same real rate and
bounds.

## 2. Transfer of the horizontal integral to the finite sum

The [exact full-period residue identity](research_mixed_pair_full_period_contour.md)
retains a fixed interval of low \(j\)-indices, extends the first
index to its full original period by exact factorial zeros, and
gives nine contour terms. It uses the upper-base residue formula
in \(x\), the lower-base formula in \(y\), and the exact combined
vertical-side multiplier. Its two fixed heights are
\[
       H=\Im x_*>0,
       \qquad K=-\Im y_*>0.
\]
The principal term lies at \((\Im x,\Im y)=(H,-K)\).

The original-index tails have a uniform real rate at most \(19/25\)
and a uniform small-strip rate at most \(77/100\). The
[horizontal maximum theorem](research_mixed_two_crossing_horizontal_dominance.md)
proves that the principal phase has its unique maximum at the
selected point on the entire real-coordinate rectangle. Its
nonzero Gaussian coefficient is precisely (3). The uniform
half-plane factorial continuation includes the added portion with
\(\Re(x+y)>1\), as well as the displaced half-grid endpoints.
Those portions avoid the critical point and retain a strict gap.

On this principal contour, the product of its two rational kernels
is
\[
             1+O(e^{-2\pi NH}+e^{-2\pi NK}).            \tag{8}
\]
Thus keeping every Fourier correction in those kernels changes
neither the Gaussian coefficient nor its power of \(N\). The
principal summand interpolation has factor \(N^{-1}\); the
residue identity supplies \(N^2\), and its two-dimensional Gaussian
supplies \(N^{-1}\). The total power is zero, as in (4).

The remaining eight contour families are estimated in
[the complete contour-face proof](research_mixed_pair_contour_face_bounds.md).
It includes their exact lattice penalties and the nonconstant
multiplier on the combined sides. At the actual finite endpoints,
every one has rate below \(113/100\), whereas
\(M>613/500\). The estimates bound the exact factorial integrands
also on zero-height portions and on moving-zero faces; a bulk
expansion at those endpoints is not used.

On a sufficiently small fixed complex disk in \(u\), their rates
remain below \(23/20\), while \(\Re S(u)>6/5\). The original tails
retain an even larger gap there. Consequently the sum of all
nonprincipal terms is bounded by a fixed polynomial times
\(e^{23N/20}\), exponentially smaller than the main term. The
ordinary holomorphic Gaussian expansion of the principal term
therefore proves (4) for the original finite source. In particular
the coefficient in (3) survives the exact contraction. Holomorphic
Cauchy estimates give the derivative statement.

This argument compares a complete list of terms in an exact
identity. It does not infer dominance merely from the local
Hessian, and no endpoint or alias sector is removed without its
bound.

## 3. The boundary curvature

The phase (2) is even in \(u\). Its critical branch is unique near
zero, so \(x(u),y(u)\) and \(S(u)\) are even. At zero, the mixed
derivatives \(W_{xu}\) and \(W_{yu}\) vanish. The envelope derivative
therefore gives
\[
 S''(0)=b_{uu}(y_*,0)
       =-\int_0^{y_*}\frac{dw}{2\cos^2(\pi w)}
       =-\frac{\tan(\pi y_*)}{2\pi}.
\]
The integral follows the same regular branch as \(b\). If
\(y_* =\xi+ih\), then
\[
 \Re\tan(\pi y_*)=
 \frac{\sin(2\pi\xi)}{\cosh(2\pi h)+\cos(2\pi\xi)}>0,
\]
because \(0<\xi<1/2\). This proves (6) independently of a numerical
Hessian value. It also supplies a local quadratic real loss after
shrinking the holomorphic disk.

## 4. The full real angular bound

The retained \(y\)-interval lies inside
\([\epsilon/2,1/2-\epsilon/2]\), where \(\epsilon=10^{-6}\), at
every sufficiently large level. All of its contour heights obey
\(|\Im y|\le K\). The uniform reciprocal-factorial theorem gives
the original Newton factor, on every one of the nine contours,
the additional loss
\[
 c_0(1-\cos u),\qquad
 c_0=\frac{\sin(\pi\epsilon)}{4\pi\cosh^2(\pi K)}>0,
                         \quad -\pi\le u\le\pi.        \tag{9}
\]
This is Section 4 of
[the factorial and boundary-decay theorem](research_uniform_factorial_and_boundary_decay.md).
It remains valid when a reciprocal factorial has a zero, and on
both signs of the wire height. All other factors and all contour
multipliers are independent of \(u\).

The principal real rate is at most \(M\). Its displacement by
\(1/(2N)\) changes this bound by only \(O(\log N/N)\), absorbed
in a polynomial prefactor. Each of the other terms has a fixed
gap below \(M\) and the same loss (9). The original omitted-index
tails have real rate at most \(19/25\). Choose
\[
                         c_1=\min(c_0,1/100).
\]
Since \(M>613/500\), those tails also obey the weaker bound with
rate \(M-c_1(1-\cos u)\). Summing all terms proves
\[
 |Z_N(u)|\le C N^d e^{N\{M-c_1(1-\cos u)\}}
                                      \quad(u\in\mathbb R).    \tag{10}
\]
This whole-period estimate applies to the original polynomial, not
only to its low-index terms or to the selected integral.

## 5. A fixed complex strip

Here is an explicit way to combine (10) with the local asymptotic.
Write \(z=e^{it}\). The function
\(z^D Z_N(t)\), \(D=N-1\), is a polynomial in \(z\) of degree at
most \(2D\). On the unit circle, (10) bounds its modulus by
\(CN^d e^{N(M-c_1+c_1\Re z)}\). Apply the maximum principle to
this polynomial times \(e^{-Nc_1z}\). For \(v\ge0\) it gives
\[
 |Z_N(a+iv)|\le C N^d
  \exp N\{M-c_1+c_1e^{-v}\cos a+v\}.                  \tag{11}
\]
Evenness gives the same bound with \(|v|\) in the lower half-plane.
Compared with the real exponent in (10), its extra cost is at most
\((1+c_1)|v|\).

Fix a small \(r_0>0\) inside the local disk of (4). For
\(|a|\ge r_0\), choose a fixed strip width so small that
\((1+c_1)|v|\le c_1(1-\cos r_0)/2\). Then (11) retains at least
half the real angular loss. For \(|a|\le r_0\), (4), evenness,
the curvature (6), and bounded higher phase derivatives give
\[
                    \Re S(a+iv)\le M-a_0a^2+B_0v^2
\]
on a fixed smaller disk, with \(a_0>0\). The nonzero amplitude
and the uniform normalized error only cost a fixed prefactor.
Combining these two regions gives (5), after reducing \(c,b\) and
increasing \(B\) if needed. Every chosen width is independent of
the level.

## 6. What this permits after attachment

The exact source (1) now satisfies the same analytic eligibility
conditions as the previously proved one-boundary blocks: a nonzero
holomorphic asymptotic, positive real boundary curvature, a whole
real angular gap, and a fixed Gaussian strip bound. Its negative
partner does as well by coefficient conjugation. Thus these actual
sources may be used in the proved fixed-crossing multiplication
and product theorem, or in the analytic part of the large-valence
composition theorem, with all of their original phases retained.

This does not assert that the turn preserves every concentrated
source. The counterexample in the
[multiplication theorem](research_boundary_crossing_packet_preservation.md)
still applies. The result here treats this particular mixed word by
its exact joint contour, rather than by an unrestricted turn rule.

Finally, (7) is an exponential rate identity for this original
boundary source. The [marked collar proof](research_mixed_word_collar_representation.md)
supplies its literal geometric attachment, original primitive
periods and absolute volume normalization. Combined with the
scalar closing theorem, it proves the volume conjecture for
the specified mixed word followed by every sufficiently long
fixed odd final power. A use inside a larger composition must
also retain that composition's interface maps and carrier
allocation; the analytic estimate alone does not supply them.

## 7. Finite normalization diagnostics

The exact coefficient and boundary-derivative checks, together with
the horizontal and face certificates, are linked in the three
companion proofs. An additional
[asymptotic normalization script](../experiments/check_mixed_two_crossing_asymptotic.py)
evaluates the full original vector \((M^2)^*M^2e_0\), without
discarding any coefficient, and compares it with (3)--(4). Run

```sh
python3 experiments/check_mixed_two_crossing_asymptotic.py --precision 120 \
  --output repro/results/research-mixed-two-crossing-asymptotic.json
```

The [saved record](../repro/results/research-mixed-two-crossing-asymptotic.json)
contains 18 comparisons at levels \(24,25,48,49,96,97\), at zero and
two displayed complex boundary arguments. At zero the finite-to-leading
ratios at levels \(24,48,96\) are approximately
\(1.055913-0.012537i\), \(1.027407-0.006128i\), and
\(1.013574-0.003028i\). These check the stated coefficient and the
absence of an additional parity unit. The samples neither prove the
asymptotic nor determine a radius for its holomorphic disk; those
claims use the contour proof.
