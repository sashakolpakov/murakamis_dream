# The exact finite-Laplace current of the canonical source

This private note constructs finite contour integrals of the canonical
Borel source and computes their exact defect under the actual quantum
operator. The defect is an endpoint exponential times a holomorphic
amplitude. No estimate at infinite Borel distance is needed. At the
ordinary meridian, a further exact identity compares the cutoff integral
with each original finite-color polynomial.

## 1. The canonical source on a finite path

Use the natural meridian of [F] and the parameter of [G]:

\[
 h=\log Q,\qquad
 \widehat{\mathscr W}(h,Y)=\sum_{j\ge0}h^j w_j(Y),\qquad
 b(Y,\xi)=\sum_{j\ge0}w_j(Y){\xi^j\over j!}.
 \tag{1}
\]

[G] gives an actual holomorphic Borel germ on every compact meridian
set avoiding zero and the Alexander divisor. [J] also supplies jointly
continued germs along its finite punctured paths near a transverse
Alexander node. The following construction applies to any finite
piecewise smooth path \(\gamma\) from \(0\) to \(R\ne0\) along which
the germ (1) has been continued jointly with a common meridian disk.
All path histories and branches are retained. A sufficiently short
path in the original germ always qualifies.

For the continued paths of [J], fix a small nonzero \(z_0\), put
\(Y=\alpha+z\), and scale a finite \(\eta\)-path by \(\xi=z_0^2\eta\).
After shrinking a disk about \(z_0\), the paths \(\xi/z^2\) remain
in the same finite continuation charts. The identity
\(b(Y,\xi)=z^{-1}\mathcal B^{\rm pole}(z,\xi/z^2)\) then gives a
common fixed \(\xi\)-path and meridian disk of the required kind.

Precisely, take a disk \(D_1\Subset\mathbb C^*\) and a finite sequence
of Borel charts along \(\gamma\) on which the continued \(b\) is
jointly holomorphic. Its values on the path and on a slightly smaller
closed meridian disk have a finite uniform bound. Shrink meridian
disks further below when applying derivatives or small shifts.

Let an actual finite-shift annihilator of (1) be

\[
 \mathcal P(h)=\sum_{i\in J}p_i(h,Y)T^i,
 \qquad T f(Y)=f(e^hY),
 \qquad \mathcal P\widehat{\mathscr W}=0,
 \tag{2}
\]

with \(J\subset\mathbb Z\) finite and \(p_i\) holomorphic on the
chosen coefficient chart near \(h=0\). Coefficients stand on the left.
This is the actual source annihilator supplied by [F]; composing an
original normal-state operator on the right with \(Y-1\) retains its
normal gauge and gives an operator of the form (2).

Define, for \(h\ne0\),

\[
 U_\gamma(h,Y)={1\over h}\int_\gamma e^{-\xi/h}b(Y,\xi)\,d\xi.
 \tag{3}
\]

It is holomorphic in \(h\ne0\) and in the smaller meridian disk.
There exists a function \(J_\gamma(h,Y)\), holomorphic and bounded
also at \(h=0\), such that exactly

\[
                 \mathcal P(h)U_\gamma(h,Y)
                         =e^{-R/h}J_\gamma(h,Y).
 \tag{4}
\]

The formula below specifies this current, including its endpoint
history. On closed subsectors where \(\Re(R/h)\ge c/|h|\) for some
\(c>0\), (4) is an exponentially small absolute operator defect.
It is not a relative error estimate
for \(U_\gamma\), nor an identification with an infinite Laplace sum.

## 2. Finite primitives and the whole operator

Let \(I\) denote integration in \(\xi\) from zero along the same
continued path. For every integer \(n\ge1\), repeated primitives obey

\[
 I^n f(\gamma(t))={1\over(n-1)!}
   \int_0^t[\gamma(t)-\gamma(s)]^{n-1}
              f(\gamma(s))\gamma'(s)\,ds.
 \tag{5}
\]

This remains true for paths with loops. If \(\gamma\) has length
\(L\), then \(\|I^n f\|\le L^n\|f\|/n!\) on the path.
Write \(\mathcal L_\gamma f=h^{-1}\int_\gamma e^{-\xi/h}f\,d\xi\).
Integration by parts retains the upper endpoint and gives

\[
 \mathcal L_\gamma(If)
       =h\mathcal L_\gamma f-e^{-R/h}If(R),
 \tag{6}
\]

because the original primitive vanishes at its initial point.
Iteration gives the exact identity

\[
 \mathcal L_\gamma(I^n f)
 =h^n\mathcal L_\gamma f
   -e^{-R/h}\sum_{j=0}^{n-1}h^j I^{n-j}f(R).
 \tag{7}
\]

Expand the actual finite shifts, rather than an abstract formal
operator:

\[
 \mathcal P(h)=\sum_{n\ge0}h^n L_n,
 \quad L_n=\sum_{\ell=0}^n a_{n\ell}(Y)\partial_Y^\ell,
 \quad
 \sum_{n\ge0}h^n a_{n\ell}(Y)
 ={1\over\ell!}\sum_i p_i(h,Y)[Y(e^{ih}-1)]^\ell.
 \tag{8}
\]

The integer \(i\) in the exponential is the shift label. In
particular there is no imaginary-unit factor in \(e^{ih}\).
The constant differential operator is multiplication by
\(\sum_i p_i(0,Y)\), which vanishes because it annihilates
\(w_0=\Delta_K^{-1}\). Hence \(L_0=0\).

On nested meridian disks \(D_0\Subset D_1\), the actual analytic compositions
\(p_i(h,Y)b(e^{ih}Y,\xi)\) are bounded for a fixed small \(h\)-disk,
uniformly along the finite Borel path. Cauchy's estimate in \(h\)
therefore gives constants \(M,C>0\) such that

\[
                  \sup_{Y\in D_0,\xi\in\gamma}|L_n b(Y,\xi)|
                                \le M C^n.       \tag{9}
\]

Equivalently, (8) retains the \(1/\ell!\) that cancels the meridian
Cauchy derivative factor. All coefficients and shifts of the original
operator are included in this estimate.

The Borel transform of its formal source equation is

\[
                       \sum_{n\ge1} I^n L_n b=0.
 \tag{10}
\]

By (5) and (9) the series converges normally on the finite path and
nearby charts. It is zero in the original germ, so analytic continuation
makes it zero on the chosen continued path. There is no free solution
or endpoint constant substituted into (10).

Applying (7) term by term proves (4) with the explicit current

\[
 J_\gamma(h,Y)=\sum_{n\ge1}\sum_{j=0}^{n-1}
                     h^j I^{n-j}L_n b(Y,R).
 \tag{11}
\]

Indeed \(\sum h^nL_n U_\gamma\) is the actual finite-shift operator
applied to (3), by the same analytic shift expansion. Writing
\(a=n-j\ge1\) in (11) gives the bound

\[
 \sup_Y|J_\gamma(h,Y)|
    \le {M(e^{CL}-1)\over1-C|h|},\qquad C|h|<1.
 \tag{12}
\]

Thus (11) is jointly holomorphic at \(h=0\); all fixed meridian
derivatives obey analogous bounds on smaller disks. Its cancellations
are retained. For example, (10) implies \(J_\gamma(0,Y)=0\).
No term of (11) has been replaced by an absolute value in the identity.

## 3. Individual shifts and analytic coefficients

An equivalent formula makes the shift current visible. Put
\(E=Y\partial_Y\) and define

\[
 c_s(Y,\xi)=e^{sIE}b(Y,\xi)
       :=\sum_{n\ge0}{s^n\over n!}I^nE^n b(Y,\xi).
 \tag{13}
\]

This series is jointly holomorphic for \(s\) in every fixed compact.
To check it directly, take a logarithmic meridian coordinate on a
larger disk, so \(E=\partial_u\). Cauchy's estimate gives
\(\|E^n b\|\le M n!d^{-n}\) on a smaller disk, while (5) contributes
\(L^n/n!\). The series (13) is then bounded by
\(M\exp(|s|L/d)\). Shrinking once more justifies its derivatives and
\(\partial_s c_s=IEc_s\).

Let \(u_s=\mathcal L_\gamma c_s\). Equation (6) gives

\[
 \partial_s u_s=hE u_s-e^{-R/h}EIc_s(Y,R),\qquad u_0=U_\gamma.
 \tag{14}
\]

Solving this ordinary transport equation with its original initial
value yields, for every fixed signed shift \(i\),

\[
 u_i=T^iU_\gamma-e^{-R/h}K_i(h,Y),\qquad
 K_i(h,Y)=\int_0^i
       (EIc_s)(e^{(i-s)h}Y,R)\,ds.
 \tag{15}
\]

The integral is oriented from \(0\) to \(i\), also when \(i<0\).
The amplitude \(K_i\) is holomorphic at \(h=0\). Small shifts stay
inside the original meridian disk after it is shrunk.

For \(p_i(h,Y)=\sum_{m\ge0}p_{im}(Y)h^m\), define

\[
 A_i(h,Y)=\sum_{m\ge1}p_{im}(Y)
                 \sum_{a=1}^m h^{m-a}I^a c_i(Y,R).
 \tag{16}
\]

These series also converge holomorphically near \(h=0\). For example,
\(|p_{im}|\le P\rho^{-m}\) and a bound \(M_i\) for \(c_i\) give
\(|A_i|\le PM_i(e^{L/\rho}-1)/(1-|h|/\rho)\).
The left-ordered Borel equation is exactly
\(\sum_i p_i(I,Y)c_i=0\). Equations (7) and (15) consequently give

\[
               J_\gamma=\sum_i\bigl(p_i(h,Y)K_i+A_i\bigr).
 \tag{17}
\]

This is the same holomorphic current as (11). In particular the
ordinary coefficient functions are not frozen at \(h=0\), and no
boundary contribution from them or from a negative shift is omitted.

## 4. Exact comparison on each fixed-color curve

Assume now that the common meridian disk contains \(Y=1\). This is
available for sufficiently short paths by [G]. Fix a positive integer
\(L_0\); constants in this section may depend on that color.
By [F]'s exact formal restriction,

\[
 \widehat{\mathscr W}(h,e^{L_0h})=C_{L_0}(e^{h/2}).
 \tag{18}
\]

Since (13) is the Borel transform of the formal shift
\(e^{s h E}\widehat{\mathscr W}\), it follows that

\[
 c_{L_0}(1,\xi)=\mathcal B_h C_{L_0}(e^{h/2})(\xi).
 \tag{19}
\]

This is initially equality of convergent germs. The scalar on the
right is entire in \(\xi\), because the original \(C_{L_0}\) is a
finite Laurent polynomial in \(e^{h/2}\). Hence (19) remains true
along every chosen path for which the left side has been constructed.
The common meridian disk is essential; a disk near a different
Alexander point is not silently treated as containing \(1\).

For any scalar function \(C(h)=\sum_{j\ge0}c_jh^j\) analytic near
zero, direct integration of its Borel monomials gives

\[
 \mathcal L_\gamma\mathcal B_h C
      =C(h)-e^{-R/h}A_C(h,R),\qquad
 A_C(h,R)=\sum_{k,m\ge0}c_{k+m}h^k{R^m\over m!}.
 \tag{20}
\]

The amplitude is holomorphic for small \(h\). In fact if
\(|c_j|\le M_0 r_0^{-j}\), then
\(|A_C|\le M_0e^{|R|/r_0}/(1-|h|/r_0)\).
To verify (20), integrate \(\xi^j/j!\) and obtain
\(h^j-e^{-R/h}\sum_{k=0}^j h^kR^{j-k}/(j-k)!\); the displayed
bound justifies both sums. No infinite Laplace contour is used.

Apply (15) at \(i=L_0,Y=1\), then (19)--(20). One obtains the exact
original-color cutoff identity

\[
 U_\gamma(h,e^{L_0h})
 =C_{L_0}(e^{h/2})+e^{-R/h}H_{\gamma,L_0}(h),
 \quad
 H_{\gamma,L_0}=K_{L_0}(h,1)-A_{C_{L_0}(e^{h/2})}(h,R).
 \tag{21}
\]

Its amplitude is holomorphic and bounded at zero. As a check retaining
the endpoint, (13) gives
\(K_{L_0}(0,1)=c_{L_0}(1,R)-b(1,R)\), whereas
\(A_C(0,R)=c_{L_0}(1,R)\). Thus

\[
                        H_{\gamma,L_0}(0)=-b(1,R).
 \tag{22}
\]

This is an exact comparison with a cutoff error, not an identification
of \(U_\gamma\) with the finite polynomial. It supplies neither a
uniform estimate as \(L_0\to\infty\) nor continuation to its complete
root-of-unity point. The original color, cut, pivot, and framing are
those of [F] throughout.

## 5. Proof sources and limits

The complete proof directs are:

| Label | Complete source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| G | notes/research_classical_verma_borel_pole_profile.md | 6ba957d7a521524f370cb3bdd90ab30338bff8c13960ae6ca1825d08260c77d2 |
| J | notes/research_classical_verma_borel_joint_continuation.md | 67cbb4c1577af04336b53985e867f6d2adc7e184c6d4276c53a0888f57d8ded8 |

F supplies the canonical formal source, actual operators, and exact
finite-color restrictions. G supplies the local Borel germ on ordinary
meridian disks. J supplies finite jointly continued paths near its
transverse node; the cutoff proof itself applies to any common finite
path as specified in Section 1. All integral identities, convergence
estimates, and cutoff comparisons are proved above.

No estimate at infinite Borel distance, moving-singularity location,
leading Stokes exponent, nonzero selected geometric coefficient, or
large-level lower bound is asserted. Only written mathematics and
source-text reads were used. Frozen notes and public manuscripts
are unchanged.
