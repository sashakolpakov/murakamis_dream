# The actual pivotal cap is a two-sided Euler coefficient functional

Research proof, 27 October 2026. This is an exact root-level statement
about the original two-leg source after the actual Borel fusion, valid
at every level. Its coefficient functional has a rational kernel with
two adjacent quantum poles. The full central-F extension has explicit
affine and wrapping corrections. None of these variables is identified
with the physical Fourier momentum or the geometric A-curve.

The starting fusion, actual cap and all external normalization lines
are those in [the actual Borel-relative period](actual_borel_regular_fusion_and_divided_cap_period.md).
In particular, no new invariant, cap normalization or preferred solution
is introduced below. A scalar normalization multiplying the original
word multiplies both sides of every period identity below.

## 1. Algebra and the original cap

Let Q have exact order N, with N at least two, over a characteristic-zero
coefficient field. Put F_j=(Q;Q)_j and F_0=1; F_(N-1)=N. Retain the
actual common highest K-eigenvalue x, assumed invertible. The actual
coproduct algebra is

\[
 A_\Phi=\langle H,f\mid H^N=1,\quad Hf=Q^{-1}fH,
                            \quad f^N=\Phi\rangle.
\]

Here f is the actual TOTAL lowering operator, not an individual
meridian clock. For two legs with actual F_i^N=phi_i,

\[
                    \Phi=\phi_1+x^{-N}\phi_2.                \tag{1}
\]

The idempotents e_j have H-eigenvalue Q^(-j). The free basis is
f^a e_j, with 0<=a,j<N, and e_j f=f e_(j-1), cyclically. Let

\[
 \tau(f^a e_j)=\delta_{a,N-1},\qquad
 \rho_0(b)=[f^{N-1}e_0]b.                                  \tag{2}
\]

The functional tau is Frobenius, but is not an ordinary cyclic trace.
It does satisfy tau(h(f)b)=tau(b h(f)) for every polynomial h(f),
because its Nakayama map fixes f. Also

\[
                    \tau(e_{N-1}b)=\rho_0(b).               \tag{3}
\]

To verify (3), left multiplication by e_(N-1) selects f^a e_j only
when j+a=N-1 modulo N; tau then selects a=N-1 and hence j=0.

Under the actual triangular fusion, the original highest-input,
all-ones-output pivotal cap has the following exact values:

\[
 \Lambda_{\rm act}(f^a e_k)=
 x^{1-N-a}Q^{-b}\frac{F_b}{F_k}
 \begin{cases}
 1,&k+a<N,\\
 \phi_2,&k+a\geq N,
 \end{cases}
 \qquad b=k+a\pmod N.                                     \tag{4}
\]

Indeed the source projector requires output weight b. Returning the
second output to its original pivotal closure forces all a lowering
steps onto that leg. Its nonwrapping coefficient is F_b/F_k; a
second-leg wrap supplies phi_2. The factors x^(1-N-a)Q^(-b) are the
original pivotal weight and K_1 inverse factors. This is the same
literal cap as before fusion. The first-leg central parameter enters
the relative algebra through (1), not through a replacement for this
second-leg wrap.

## 2. Exact two-sided Euler form on the nilpotent fiber

Write z=xf and define the finite polynomials

\[
 u(z)=\sum_{j=0}^{N-1}\frac{z^j}{F_j},\qquad
 v(z)=\sum_{j=0}^{N-1}
          \frac{(-1)^jQ^{j(j-1)/2}z^j}{F_j},\qquad
 v_2(z)=v(Q^2z),
 \quad \gamma=Nx^{2-2N}Q.                                \tag{5}
\]

On phi_1=phi_2=0, the ORIGINAL cap is exactly

\[
 \boxed{\quad
 \Lambda_{\rm act}(a)=\gamma\rho_0\big(v_2(z)\,a\,u(z)\big).
 \quad}                                                   \tag{6}
\]

The shift Q^2 is necessary. Replacing v_2 by v is false in general;
level two conceals the error since Q^2=1 there.

Here is a direct all-level proof. The cap density from the actual
fusion factors as L R, where

\[
 L=u(z)e_{N-1},\qquad
 R=\sum_{k=0}^{N-1}x^{1-N-k}Q^{-k}F_k f^{N-1-k}e_k.
\]

The elementary product identity

\[
 F_{N-1-j}=N\frac{(-1)^jQ^{j(j+1)/2}}{F_j}
\]

gives R=gamma e_(N-1)v_2(z), coefficient by coefficient. Thus
the exact density is C=gamma u(z)e_(N-1)v_2(z). Moving u through
tau, which is permitted for polynomials in f, and then using (3)
proves (6). This derivation uses the actual cap density, rather
than prescribing a desirable co-source afterward.

The finite Euler equations on this nilpotent fiber are

\[
 u(Qz)=(1-z)u(z),\qquad v(z)u(z)=1.
\]

For degrees below N the first follows by subtracting consecutive
coefficients; its remaining degree-N term vanishes because z^N=0.
The second follows either by the finite q-binomial formula or by
the same recurrence and constant term one. Consequently

\[
 v_2(z)u(z)=\frac1{(1-z)(1-Qz)}=:J_Q(z),                   \tag{7}
\]

and (6) has the equivalent exact form

\[
 \boxed{\quad
 \Lambda_{\rm act}(a)=\gamma\rho_0
       \left[J_Q(z)\,u(z)^{-1}a\,u(z)\right].\quad}        \tag{8}
\]

All inverses in (7)-(8) exist in the truncated algebra: their
arguments have constant term one and z is nilpotent. Formula (8)
is a coefficient identity with a rational kernel; it does not
introduce a convergent contour integral or an asymptotic cycle.
In particular J_Q must be applied AFTER the indicated actual-word
Euler conjugation. Inserting it as an extra weight in the old
unconjugated word would change the period.

For any actual two-leg word W that commutes with the diagonal
Borel action, its fused action is right multiplication by the
unique element a_W. The original period, with its original
external line gamma_W, is therefore exactly

\[
 P_W=\gamma_W\gamma\rho_0
       \left[J_Q(z)u(z)^{-1}a_Wu(z)\right].                \tag{9}
\]

This applies to words, their signed inverses and their exact
compositions. It is not limited to a chosen critical branch.
There is a relevant left/right distinction. Physical total F
acts by LEFT multiplication on this free fused module, whereas
a_W is its RIGHT-multiplication coefficient. Thus the conjugation
a_W -> u^(-1)a_W u in (8) is in the right coefficient algebra.
It is not conjugation of the physical word by u(physical total F):
the latter commutes with a Borel-linear word and would do nothing.
For more than two legs the actual free relative module has
matrix-valued word coefficients and its original entry-dependent
cap rows; those rows must be retained. No assertion that all
of them equal this single two-leg cap is being made.

## 3. The whole central-F extension retains its wrap correction

Equations (5) still define polynomials on the full flat A_Phi
family. Define

\[
 C_E=\gamma u(z)e_{N-1}v_2(z),\qquad
 \Lambda_E(a)=\tau(C_Ea)=\gamma\rho_0(v_2(z)a u(z)),
\]

and the explicit element

\[
 W=\sum_{a=1}^{N-1}\sum_{b=0}^{a-1}
 x^{1-N-a}Q^{-b}\frac{F_b}{F_{N+b-a}}
                        f^{N-1-a}e_b.                   \tag{10}
\]

Then the exact ORIGINAL whole cap is

\[
 \boxed{\quad
 C_{\rm act}=C_E-x^N\phi_1 W,\qquad
 \Lambda_{\rm act}(a)=\Lambda_E(a)-x^N\phi_1\tau(Wa).
 \quad}                                                  \tag{11}
\]

This correction is essential even when Phi=0: opposite nonzero
leg centers can have zero total center.

To prove (11), evaluate the Euler density on f^a e_k. The
idempotent in u e_(N-1)v_2 forces the coefficient of u to have
index k and that of v_2 to have index N-1-b, where b=k+a mod N.
If k+a<N, their total f degree, including a, is N-1. The value
is the first case of (4). If k+a>=N, that degree is 2N-1 and
one factor Phi occurs. The resulting value is

\[
 \Lambda_E(f^a e_k)=x^{1-N-a}Q^{-b}\frac{F_b}{F_k}
 \begin{cases}1,&k+a<N,\\ x^N\Phi,&k+a\geq N.\end{cases} \tag{12}
\]

The Frobenius dual-basis formula makes tau(W f^a e_k) zero in
the first case and x^(1-N-a)Q^(-b)F_b/F_k in the second.
Now use x^N Phi=x^N phi_1+phi_2. Equations (4), (11) follow
on every basis element, hence on the whole flat family.

The Euler density itself has a useful exact central scalar:

\[
 e_{N-1}v_2(z)u(z)e_{N-1}=d\,e_{N-1},\qquad
 d=1+\frac{N-3}{2N}x^N\Phi,\qquad C_E^2=\gamma d C_E.     \tag{13}
\]

Only total degrees zero and N contribute in this corner. The
degree-N coefficient of v_2(z)u(z) is

\[
 -\frac1N\sum_{j=1}^{N-1}\frac{Q^{2j}}{1-Q^j}
                         =\frac{N-3}{2N}.
\]

For the last equality use sum 1/(1-Q^j)=(N-1)/2,
sum Q^j=-1 and t^2/(1-t)=1/(1-t)-1-t. This proves (13),
including composite N. If phi_1=0, C_act=C_E and the same
quadratic relation holds for the actual cap. In general its
explicit W correction cannot be discarded. In particular d
is not the multiplicative Euler norm 1-x^N Phi.

## 4. Exact dressed source Ward equation and its affine completion

Let sigma fix H,x and send f to Qf. This is an algebra
automorphism, with sigma=Ad(H inverse). Put

\[
 t=1-z,\qquad t_2=1-Q^2z,\qquad c=x^N\Phi/N.
\]

Direct comparison of consecutive coefficients in (5), including
the last degree, gives the WHOLE polynomial equations

\[
 \boxed{\quad \sigma u=t u+c,\qquad
                         t_2\sigma v_2=v_2-c.\quad}       \tag{14}
\]

The last coefficients are respectively +z^N/N and -z^N/N.
They are not zero away from the nilpotent source.

On the open chart 1-x^N Phi invertible, t_2 is invertible since
its cyclic product is 1-x^N Phi. For any a put

\[
 V=t_2^{-1}\sigma(a),\qquad
 T(a)=Vt,\qquad \delta(a)=T(a)-Q^{-1}a.                   \tag{15}
\]

Then the exact actual co-source equation is

\[
 \boxed{\begin{aligned}
 \Lambda_{\rm act}(\delta(a))
 &=\gamma c\rho_0\big(Vtu+cV-v_2V\big)
                         -x^N\phi_1\tau(W\delta(a)).
 \end{aligned}}                                          \tag{16}
\]

For a proof, put b=v_2 a u. Equation (14) gives, with the
noncommutative order retained,

\[
 v_2T(a)u-\sigma(b)=c\big(Vtu+cV-v_2V\big).
\]

Since rho_0(sigma b)=Q^(N-1)rho_0(b)=Q^(-1)rho_0(b),
applying gamma rho_0 and then (11) proves (16).

On the actual nilpotent source phi_1=phi_2=0, both right-hand
terms vanish. Thus this is the exact dressed Ward identity

\[
           \Lambda_{\rm act}(T(a)-Q^{-1}a)=0.              \tag{17}
\]

It is a statement about the ORIGINAL cap, not just a homogeneous
formal solution. At nonzero centers (16) specifies the affine
defect and the source's first-leg wrap term. Treating (17) as
homogeneous on that whole family would erase actual source data.

## 5. The source connection in x is also explicit

At phi_1=phi_2=0 define

\[
 A=\sum_{r=1}^{N-1}\frac{x^{r-1}f^r}{1-Q^r},\qquad
 A_2=\sum_{r=1}^{N-1}\frac{Q^{2r}x^{r-1}f^r}{1-Q^r}.
\]

The finite Euler equation gives u^(-1)partial_x u=A and
partial_x v_2=-A_2 v_2. For example, take the nilpotent
logarithm in u(Qz)=(1-z)u(z): in degree r<N its coefficient
is 1/[r(1-Q^r)], which proves these formulas by differentiation.
Differentiating (6) therefore gives exactly

\[
 \partial_x\Lambda_{\rm act}(a)
 =\frac{2-2N}{x}\Lambda_{\rm act}(a)
    +\Lambda_{\rm act}(\partial_xa+aA-A_2a).              \tag{18}
\]

The scalar gamma character has been retained. In particular
(18) agrees with the x^(1-N-a) dependence of every original
basis cap value in (4). This is an x-connection at the fixed
root, not an identification with the moving-q normal direction.

## 6. What this does and does not resolve on the critical path

This result supplies an exact actual-word/source transform with
a rational coefficient kernel. It removes the need to guess an
unsourced double-pole weight for the two-leg Borel cap. It also
locates all central-F affine and wrapping defects before taking
jets. These are useful prerequisites for a selected-period map.

The equality z=xf is an operator in the TOTAL lowering algebra.
It has not been identified with the physical second-meridian
Fourier variable p, nor with a coordinate on the geometric
critical variety. Similarity between J_Q and a geometric density
with a double pole is not such an identification. The actual
word is Euler-conjugated in (8), and the central correction in
(11) is not optional. The fixed-root central-F family also does
not contain the moving-q divided-power normal automatically.

Thus the next required bridge is an actual source-compatible
symbol/period transform from the dressed word and cap in (8)
(or its full relative matrix source) to the geometric
meridian/A-period object. That map must carry actual source
currents to zero and send the original selected class to a
proved nonzero geometric class. This note constructs no such
map, and proves neither its subexponential coefficient nor the
global volume norm. Gates C, D and E remain open.

## 7. Exact checks

The [audit](../experiments/audit_actual_euler_cap_boundary.py)
and [saved output](../experiments/actual_euler_cap_boundary_results.json)
were rerun successfully at N=2,...,7. The checks use the literal
original physical cap after triangular fusion, not a cap defined
by the answer (6). They cover 139 nilpotent basis Cauchy/connection
identities and 139 explicit rational-kernel coefficient identities,
556 whole cap basis values across four central
specializations per level, 24 whole Euler/wrap cases, 500 affine
co-source Ward identities on their invertible charts, and 24
literal signed-word period tests. The proofs above are all-level;
these exact finite-field tests are independent convention and
coefficient checks, not a substitute for those proofs.
