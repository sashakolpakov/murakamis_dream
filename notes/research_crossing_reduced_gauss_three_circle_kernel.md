# An actual three-circle coefficient for the crossing-reduced Gauss kernel

Private written proof, 18 November 2026.

The exact replacement of a physical crossing by \(E^HF^H\) admits
a nonzero coherent coefficient on an explicit open complex domain.
The original two Euler coefficient circles and the physical
occupation circle select a single saddle. Their entire complements
are estimated with the finite caps retained.

The complementary fraction \(H/N\) is small and positive, and the
estimates are uniform on its fixed compact subintervals. There is no
uniform assertion as \(H\) stays bounded. The external domain
is described below; it is not identified with a geometric knot
representation. Meridian normals and the remaining exterior are
not covered.

## 1. Actual finite coefficient and external domain

Use the complete directs C and F pinned below. At the fixed root set
\[
 c_0=2\pi i,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 d=N-1,\quad x=-q^{-1},\quad f_n=(Q;Q)_n.
 \tag{1}
\]
On two original heads use F's ordered totals
\[
 E=E_1K_2+E_2,\qquad F_{\rm tot}=F_1+K_1^{-1}F_2.
\]
We abbreviate the latter by \(F\) below. The coherent row and the
ordinary-binomial input are exactly
\[
 v(w)w_a=w^a,\qquad c(z)=\sum_{a=0}^d\binom da z^a w_a,
 \tag{2}
\]
with tensor products on the two heads. Let \(\Pi_T\) be the literal
integer-degree projector. For \(H=d-T\) define
\[
 \mathcal P_{N,T,H}(w,z)
       =v(w_1,w_2)E^HF^H\Pi_Tc(z_1,z_2).
 \tag{3}
\]
Since \(E^HF^H\) preserves total degree, (3) is its actual
degree-\(T\) coherent kernel. No spectral projection is inserted.

Fix a base point with
\[
 w_i^0>0,\quad z_i^0>0,\quad
 r_i^0=w_i^0z_i^0,\qquad r_1^0\ne r_2^0.
 \tag{4}
\]
There is a complex neighborhood \(\mathcal O\) of this point and a
number \(\alpha_0>0\) with the following conclusion. Put
\[
 \alpha=H/N,\qquad \tau=T/N=1-\alpha-N^{-1}.
 \tag{5}
\]
For physical integers \(H,T\) and \(\alpha\) in any fixed compact
subinterval of \((0,\alpha_0)\), the kernel (3) has the actual
nonzero asymptotic (25) below, uniformly on smaller compact
subsets of \(\mathcal O\), with every fixed external derivative.
The constants may depend on that compact \(\alpha\)-interval.
Take \(\alpha_0<1/2\), so F's upper-chamber factorization applies.

For independent coefficient variables \(u,v,s\), put
\[
 \mathcal G_N(u,v;s)=
  v(w)E_N(uE)E_N(vF)c(sz),\qquad
 E_N(tX)=\sum_{n=0}^d t^nX^n/f_n.
 \tag{6}
\]
Here \(sz=(sz_1,sz_2)\); all three letters in (6) are auxiliary
coefficient variables, not the meridian. Direct finite coefficient
extraction gives
\[
 \boxed{\quad
 \mathcal P_{N,T,H}
       =f_H^2[u^Hv^Hs^T]\mathcal G_N(u,v;s).
 \quad}\tag{7}
\]
This is the integral over three positively oriented circles about
zero, with denominators \(u^{H+1}v^{H+1}s^{T+1}\).
It is exact before any contour estimate. Every cap and binomial
factor in (2),(6) is still present.

## 2. The mixed Euler kernel on the entire required annulus

We first verify the input needed from C, rather than using divisor
avoidance as a substitute for a kernel theorem. Its conclusion,
extended to the finite mixed list below by its same proof, is
\[
 \frac{\mathcal G_N(u,v;s)}
        {(1+sr_1)^d(1+sr_2)^d}
   =e^{N\mathcal S(u,v;s,w,z)}
       b(u,v;s,w,z)(1+O(N^{-1})),
 \tag{8}
\]
where \(r_i=w_iz_i\), \(\mathcal S(0,0)=0\), \(b(0,0)=1\), and
\(b\) is a holomorphic unit. This holds for sufficiently small
independent \(u,v\), uniformly on any specified compact set of
nonincident external pairs \((w_i,sz_i)\).
All fixed derivatives have the same relative estimate on smaller
domains.

Here are the details that allow both signs of the total arrow.
On one head the root balanced turn
\(\mathscr Ww_a=(-1)^aw_{d-a}\) is induced by a fixed projective
linear map in the binomial coherent model. It interchanges \(E,F\)
and inverts \(K\). Tensor reversal followed by these turns sends
the ordered total \(E\) to the ordered total \(F\), with no
additional scalar. Hence C's actual local lowering-factor kernels
give the raising-factor kernels by this exact finite conjugation.
It preserves incidence and the original finite coherent resolution.

There is also a direct check of C's global hypothesis. On homogeneous
polynomials \(p(W_0,W_1)\) of degree \(d\),
\[
 \begin{split}
 Ep(W)&=W_0\{p(W_0,Q^{-1}W_1)-p(W)\}/W_1,\\
 Fp(W)&=W_1\{p(W)-p(Q^{-1}W_0,W_1)\}/W_0.
 \end{split}\tag{9}
\]
The second equality uses \(Q^{d+1}=1\); its apparent division is
removable. Both are derivatives integrated over a coordinate arc
of length \(O(N^{-1})\). For example, with \(\delta=Q^{-1}-1\),
\[
 Fp(W)=-\delta W_1\int_0^1
        (\partial_0p)((1+t\delta)W_0,W_1)\,dt.
 \tag{10}
\]
After any fixed projective conjugation these remain bounded
rank-one derivative fields along short linear maps. Iterating \(n\)
times gives C's exact low-power estimate
\[
 |K_{X^n}(W,Z)|\le C_g^n
       (|WZ|+C_gn/N)^{d-n}
 \tag{11}
\]
on the active head, with the original short Cartan rotations on
the spectators. The factor \(N^{-n}(d)_n\) has already been
bounded in (11). When a link is separated, the same bound has
an \(e^{-cN}\) factor for \(n\le\delta_0N\).
It includes independent links at incidence.

For larger \(n\), C's actual matrix bound on a fixed small activity
circle and its Cauchy tail estimate apply also after the turn.
Its possible \(e^{C_gN}\) coherent-conditioning cost is beaten by
shrinking the activity. Thus every mixed factor has C's global
bounds \(e^{CN(|u|+|v|)}\), and a separated link has an additional
fixed exponential gap. The finite list consists of the ordered
coproduct factors for \(E\), followed by those for \(F\).

Insert the exact compact resolutions between this finite mixed list.
After C's external projective adaptation, at zero activities all
links are identity links, with the same unique maximum and positive
real-part chain quadratic. The separated-link bounds just proved
pay the entire complement, including cross-link incidence.
C's compact cutoff deformation and complex Gaussian calculation
therefore apply to this mixed list. The complex chain determinant
is one; no new Gaussian multiplicity or orientation occurs.

Finally the root cap comparison in C replaces the factor products
by the actual total polynomials in (6). The raising comparison is
the conjugate of the lowering one. In a difference of the two
products, multiply each exponentially small carry by the norm of
the other total, at most \(e^{CN(|u|+|v|)}\). C's arbitrarily strong
carry rate, obtained by reducing the activity, pays this factor
and the coherent-conditioning cost. This proves (8) for the
literal two polynomials, with all caps. It is not a specialization
of an untruncated generic-\(q\) product identity.

The local functions in (8) glue on a compact annulus in \(s\).
For large \(N\) the exact normalized kernels are nonzero on the
small activity polydisk times that annulus and equal one at
\(u=v=0\). Their winding along an \(s\)-loop is consequently zero
by that activity homotopy. Their normalized logarithms therefore
exist there. The locally constructed limits \(\mathcal S,b\),
with \(\mathcal S(0)=0,b(0)=1\), agree on overlaps by these
logarithms and the uniform asymptotic. There is no reset of a
phase mark while traversing the \(s\)-circle.

For the domain (4), define \(s_0=s_0(\tau,w,z)\) by
\[
        \frac{s_0r_1}{1+s_0r_1}
       +\frac{s_0r_2}{1+s_0r_2}=\tau.
 \tag{12}
\]
At the base point and \(\tau=1\),
\(s_0=(r_1^0r_2^0)^{-1/2}>0\).
Its logarithmic derivative in (12) is strictly positive. The
analytic implicit function theorem defines \(s_0\) for \(\tau\)
near one and \(w,z\) in a fixed smaller complex neighborhood.
At the base point neither \(s_0r_i^0\) equals one, by (4).
There is consequently a compact annulus around the entire family
\(s=s_0e^{i\theta}\), with a slightly larger annular neighborhood,
on which both \(1+sr_i\) remain bounded away from zero.
This verifies that all external pairs lie in a single compact
subset of C's nonincidence space throughout the contour.
Thus (8), its global finite-cap proof, and its fixed derivative
bounds apply on the entire annulus with one activity radius.

## 3. The nonzero initial Euler slopes

Put
\[
 \theta_i=\frac{sr_i}{1+sr_i},\qquad A_i=e^{-c_0\theta_i}.
\]
The exact coherent one-head clock formulas at the root give the
principal arrow values
\[
 e_i=(A_i-1)/w_i,\qquad
 f_i=w_i(1-A_i^{-1}),\qquad k_i=-A_i.
\]
With the original total order,
\[
 e=-A_2(A_1-1)/w_1+(A_2-1)/w_2,\qquad
 f=w_1(1-A_1^{-1})-A_1^{-1}w_2(1-A_2^{-1}).
 \tag{13}
\]
Since \(f_1=1-Q=-c_0/N+O(N^{-2})\), differentiating the
literal polynomials at zero activity, or C's calibrated transport,
gives
\[
                  \mathcal S_u(0,0)=-e/c_0,\qquad
                  \mathcal S_v(0,0)=-f/c_0.
 \tag{14}
\]
No meridian differentiation is involved.

At the base \(s_0,\tau=1\), one has \(A_1A_2=1\), with
\(A_2\ne1\). Thus
\[
 e=(A_2-1)(w_1^{-1}+w_2^{-1}),\qquad
 f=(1-A_2)(w_1+w_2),
 \tag{15}
\]
both nonzero by (4). After shrinking the external neighborhood
and the range of \(\tau\), these slopes stay bounded away from
zero at \(s_0\). This verifies a nonempty actual domain; a
nonvanishing slope has not been assumed from a canonical graph.

## 4. Three original circles and their complete gap

Define, on the indicated local logarithm branches,
\[
 \Phi(u,v,s)=\log(1+sr_1)+\log(1+sr_2)
          +\mathcal S(u,v;s)-\alpha\log u-\alpha\log v-\tau\log s.
 \tag{16}
\]
Keep \(\tau\) exact as in (5). The saddle equations are
\[
 u\mathcal S_u=\alpha,\qquad v\mathcal S_v=\alpha,\qquad
 D_s\{\log(1+sr_1)+\log(1+sr_2)+\mathcal S\}=\tau.
 \tag{17}
\]
Set \(u=\alpha U,v=\alpha V\) and divide the first two equations
by \(\alpha\). At \(\alpha=0\), their solution is
\[
       U=-c_0/e(s_0),\qquad V=-c_0/f(s_0),\qquad s=s_0.
\]
The Jacobian is triangular with nonzero diagonal: the first two
entries are the slopes (14), and the last is the derivative of
(12). The analytic implicit function theorem supplies a unique
nearby saddle, with
\[
 u_*=-c_0\alpha/e(s_0)+O(\alpha^2),\quad
 v_*=-c_0\alpha/f(s_0)+O(\alpha^2),\quad
 s_*=s_0+O(\alpha).
 \tag{18}
\]
All statements are uniform for the specified external neighborhood
and \(\tau\) near one. Decrease \(\alpha_0\) so that the whole torus
\[
 (u,v,s)=(u_*e^{i\theta_u},v_*e^{i\theta_v},s_*e^{i\theta_s}),
                \qquad -\pi\le\theta_j\le\pi,
 \tag{19}
\]
lies in (8)'s activity disks and compact \(s\)-annulus.
This is a product of three positive circles about zero. The finite
polynomial in (7) has no other poles, so choosing these radii
preserves exactly the original coefficient cycle.

We give the global estimate needed on (19). At the real base,
the zero-activity occupation phase
\[
 \Phi_0(s)=\log(1+sr_1)+\log(1+sr_2)-\tau\log s
\]
satisfies
\[
 \Re[\Phi_0(s_0e^{i\theta})-\Phi_0(s_0)]
                         \le -c(1-\cos\theta).
 \tag{20}
\]
Each positive \(s_0r_i\) gives the usual factor
\[
 |1+s_0r_i e^{i\theta}|/(1+s_0r_i)
 =\{1-4s_0r_i(1+s_0r_i)^{-2}\sin^2(\theta/2)\}^{1/2}.
\]
The factors avoid zero on the full circle. For the smaller complex
external neighborhood, the exact stationarity at \(s_0\) and
bounded second derivatives preserve (20), with a smaller constant.

Outside a fixed small \(\theta_s\)-interval, (20) has a fixed
gap. The change \(s_0\mapsto s_*\) and all Euler terms are
\(O(\alpha)\) uniformly on the whole torus, so this gap persists
for small \(\alpha_0\), regardless of the other two angles.

Inside that interval, use the comparison phase
\[
 \Phi_0(s_0e^{i\theta_s})-\Phi_0(s_0)
       +\alpha(e^{i\theta_u}-1-i\theta_u)
       +\alpha(e^{i\theta_v}-1-i\theta_v).
 \tag{21}
\]
The difference between the actual phase difference and (21)
has zero value and first derivatives at the origin. Its second
derivatives in the \(s\)-direction are \(O(\alpha)\);
the mixed \(s\)-activity derivatives are \(O(\alpha)\).
At \(\theta_s=0\) the pure activity derivatives of that difference
are \(O(\alpha^2)\), by (17),(18) and the activity Taylor expansion
of \(\mathcal S\). At general small \(\theta_s\) they differ by
\(O(\alpha|\theta_s|)\).
These are uniform bounds for all activity angles in \([-\pi,\pi]\),
because their radii are \(O(\alpha)\).

Integrate these derivative estimates first along the \(\theta_s=0\) face
and then in the \(s\)-direction. They bound the difference by
\[
 C\alpha\theta_s^2+
 C\alpha|\theta_s|(|\theta_u|+|\theta_v|)
       +C\alpha^2(\theta_u^2+\theta_v^2).
\]
Use \(1-\cos\theta\ge2\theta^2/\pi^2\) on this angular interval
and the weighted Young inequality on the middle term. After
reducing \(\alpha_0\), (20),(21) therefore give
\[
 \boxed{\quad
 \Re[\Phi(u_*e^{i\theta_u},v_*e^{i\theta_v},s_*e^{i\theta_s})
                      -\Phi(u_*,v_*,s_*)]
 \le-c_1\theta_s^2-c_2\alpha(\theta_u^2+\theta_v^2)
 \quad}\tag{22}
\]
on the small \(s\)-interval. Together with the already proved
outside gap, this bounds the complete coefficient torus and shows
that its unique real maximum is the selected saddle.
This estimates the actual polynomial through (8); no cap term or
occupation sector has been deleted.

The logarithms in (16) need not be single-valued around every
circle. They are continued from the saddle on the angular cover.
Their real parts and derivative bounds above are single-valued.
The exact integrand is single-valued: \(N\alpha=H\) and
\(N\tau=T\) are integers, and \(d=N-1\) is retained in its amplitude.
A winding of either identity factor is therefore an original
integer phase, not an untracked normalization. The normalized
Euler phase in (8) has the global marking proved in Section 2.

## 5. Gaussian coefficient and exact source normalization

Write
\[
 \Psi=\Phi(u_*,v_*,s_*),\qquad
 \mathcal H=(D_iD_j[
        \log(1+sr_1)+\log(1+sr_2)+\mathcal S])_*,
       \quad i,j\in\{u,v,s\}.
 \tag{23}
\]
The linear logarithmic coefficient terms do not affect this
Hessian. At the base, with small \(\alpha>0\), it has diagonal
\((\alpha,\alpha,V_0)+O(\alpha)\), where
\[
 V_0=\sum_i\frac{s_0r_i}{(1+s_0r_i)^2}>0.
\]
More precisely its two activity diagonal corrections and their
mutual off-diagonal are \(O(\alpha^2)\), its mixed \(s\)-activity
entries are \(O(\alpha)\), and its \(s\)-entry is \(V_0+O(\alpha)\).
Thus
\[
                     \det\mathcal H=V_0\alpha^2(1+O(\alpha)).
 \tag{24}
\]
Its real part on the three angular directions is positive definite
by (22). Choose the square root by continuation from
\(\sqrt{V_0}\alpha\) at the positive base as \(\alpha\downarrow0\).

The exact numerator identity caps have power \(d=N-1\).
Consequently the full local amplitude after writing \(N\Phi\)
is
\(b(u_*,v_*;s_*)/[(1+s_*r_1)(1+s_*r_2)]\).
The coefficient measure in (7) becomes
\(d\theta_u\,d\theta_v\,d\theta_s/(2\pi)^3\).
It follows that
\[
 \boxed{\quad
 \mathcal P_{N,T,H}(w,z)=
 \frac{f_H^2 e^{N\Psi}}
      {(2\pi N)^{3/2}\sqrt{\det\mathcal H}}\,
 \frac{b(u_*,v_*;s_*,w,z)}
      {(1+s_*r_1)(1+s_*r_2)}
             (1+O(N^{-1})).
 \quad}\tag{25}
\]
Every displayed leading factor is nonzero on the stated domain.

To verify the error, fix a compact \(\alpha\)-subinterval of
\((0,\alpha_0)\). Equation (22) then gives a uniform Gaussian
gap in all three variables. Outside a small saddle neighborhood
the integral is exponentially smaller. Inside it, splitting at
radius \(N^{-2/5}\), Taylor expansion through cubic phase and
linear amplitude has vanishing odd Gaussian terms; the next
moments give relative \(O(N^{-1})\). The actual relative error in
(8) is holomorphic and uniformly \(O(N^{-1})\) on a larger
parameter set, so it gives the same order after this saddle
integration. No estimate was first continued from a discrete
matrix index. Fixed external derivatives follow by Cauchy after
shrinking the complex neighborhood. The three positive circles
pass once through the saddle, fixing the Gaussian coefficient
in (25) to one.

Finally F's exact physical crossing identity gives
\[
 v(w)A_TR_T\Pi_Tc(z)=\kappa c_H\mathcal P_{N,T,H}(w,z),
 \qquad c_H=(-1)^{d-H}Nq^{3H^2}/f_{2H}.
 \tag{26}
\]
Thus (25) estimates the actual crossing-reduced Gauss coefficient,
with this scalar and the exact factorial \(f_H^2\) retained.
The coefficient is not a scalar Casimir evaluation.

This is a physical-integer-degree, fixed-root result on the
explicit neighborhood (4) and small complementary fractions.
It does not place a chosen hyperbolic total-product flag in that
neighborhood. It does not estimate the other routed braid factors,
the original meridian finite part, or a closed-source contribution.
In particular F's normal defect remains if (26) is used inside
a meridian-dependent expression.

## Complete proof directs

* C: notes/research_capped_coproduct_compact_coherent_composition.md,
  SHA256 c54ba609e91ca18193ac9c9d7e7b32f0d0b39c00b3ff36bdf830184f8ad24d2b.
* F: notes/research_gauss_physical_crossing_factorization.md,
  SHA256 54d1b6c1e200cab6ca6e5affc49c98fe57d7c395a542d5f8afe502345884486f.

Both complete directs were freshly read nontruncated in this author
sequence. The mixed-list extension, annular hypothesis audit,
physical coefficient contour and its full gap are proved inline.
Only written mathematics and text/hash operations were used;
frozen and public files were not changed.

Author freeze protocol: the entire matching final was freshly reread
nontruncated. Both complete direct reads were retained fresh and
unchanged from this active author sequence; every used implication
was checked, and all three pins were renewed. Independent matching
review and parent adoption remain separate.

