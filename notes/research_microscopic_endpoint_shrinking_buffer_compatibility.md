# Scalar endpoint compatibility with a shrinking physical buffer

Private written proof, 16 November 2026.

The scalar compatibility theorem extends uniformly to physical
intervals whose distance from either endpoint tends to zero. The
available complex width is proportional to that distance, and the
actual normal defect is bounded by polynomial factors times
\(\exp(-cN\rho)\). A full-product bound for the exact lowering
amplitude is used near the endpoint; requiring every finite ratio
to be uniformly contracting would lose this scale.

This gives a scalar overlap at any growing index \(j=N^\kappa\),
\(0<\kappa<1\). It does not cancel a window current or control its
remaining coupled source.

## 1. Quantitative assertion and original data

Use
\[
 D=N-1,\quad\eta=(-1)^D,\quad\theta=\pi/N,\quad
 c(r)=2\cos((2r+1)\theta),\quad c_N(x)=c(Nx),
\]
\[
 w_N(\alpha)=2\cosh(\alpha/N),\quad
 F_j(\alpha)=K_N(c(j),w_N(\alpha)),\quad
 G_j(\alpha)=\partial_ZK_N(c(j),w_N(\alpha)).
 \tag{1}
\]
The kernel and Newton normalization are the original ones:
\[
 K_N(w,Z)=\sum_{k=0}^{N-1}e_k(w)e_k(Z),\quad
 e_k(Z)=S_k^{-2}\prod_{a<k}(c(a)-Z),\quad
 S_k=\prod_{a=1}^k2\sin(a\theta).
 \tag{2}
\]
Write
\[
 I_\rho=[\rho,1/2-\rho],\qquad
 U_{\rho,r}=\{x:\operatorname{dist}(x,I_\rho)<r\rho\}.
 \tag{3}
\]
All constants below are independent of \(N\) and \(\rho\).
They may depend on a fixed bound for the complex parameter and,
for shared products, on their fixed number.

**Theorem 1.** For every \(A<\infty\), there exist
\[
 M\ge1,\quad 0<\rho_*<1/16,\quad r,c>0,\quad C<\infty,\quad P<\infty
 \tag{4}
\]
such that whenever
\[
                  M/N\le\rho\le\rho_*,
 \tag{5}
\]
there are jointly holomorphic \(f_N,\mathcal G_N,h_N\) on a
neighborhood of \(\overline{U_{\rho,r}}\) and \(|\alpha|\le A\)
with
\[
 f_N(j/N,\alpha)=F_j,\qquad
 \mathcal G_N(j/N,\alpha)=G_j\qquad(j/N\in I_\rho),
 \tag{6}
\]
\[
 \|f_N\|+\|\mathcal G_N\|+\|h_N\|\le CN^P\rho^{-P},
 \tag{7}
\]
\[
 \|c_N'\mathcal G_N-\partial_xf_N\|
       +\|h_N-f_N\|
                  \le CN^P\rho^{-P}e^{-cN\rho},
 \tag{8}
\]
and exact scalar Hermite interpolation
\[
             h_N(j/N,\alpha)=F_j,\qquad
             h_N'(j/N,\alpha)=c_N'(j/N)G_j
                         \quad(j/N\in I_\rho).
 \tag{9}
\]
The constructions are defined on larger spatial and parameter
domains before (7)--(8) are asserted. Hence, for any fixed number
of \(x\)-derivatives, Cauchy's formula adds only the corresponding
power of \(\rho^{-1}\) on a smaller \(U_{\rho,r}\). Fixed parameter
derivatives have the same bounds on a smaller parameter disk.
The constants may be chosen uniformly at both parities, including
parameters where \(\cosh(\alpha/2)=0\).

In particular the polynomial factors in (8) are explicit types
of losses, not constants permitted to depend arbitrarily on the
moving buffer. The estimate is useful when \(N\rho\) dominates
their logarithms.

## 2. Uniform rescaling of the actual four-component recurrence

Let \(s_r=2\sin(r\theta)\) and set
\[
 A_N(r)=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\quad
 C_N(r)=\frac{s_r^4}{s_{2r}s_{2r+1}},\quad
 q_N(x)=\frac{C_N(Nx)}{A_N(Nx)},\quad
 d_N(x)=\frac{c(0)-w_N(\alpha)}{A_N(Nx)}.
 \tag{10}
\]
The actual value and normalized common-index normal states are
\[
 X_j=\binom{F_j}{N(F_j-F_{j-1})},\qquad
 Y_j=\binom{c_N'(j/N)G_j}
 {N[c_N'(j/N)G_j-c_N'((j-1)/N)G_{j-1}]}.
 \tag{11}
\]
The pinned two-channel theorem derives their exact bulk recurrence
\[
 X_{j+1}=T_N(j/N)X_j,\quad
 Y_{j+1}=T_N(j/N)Y_j+T_N'(j/N)X_j,\quad
 T_N=\begin{pmatrix}1+d_N&q_N/N\\Nd_N&q_N\end{pmatrix}.
 \tag{12}
\]
The prime in (12) is in \(x\). The original endpoint forcing and
its derivative vanish at these bulk nodes only; their actual
initial data remain in (11).

Set
\[
 \epsilon=(N\rho)^{-1},\qquad y=x/\rho,\qquad
 S_\rho=\operatorname{diag}(1,\rho),\qquad
 \widetilde T_N(y)=S_\rho T_N(\rho y)S_\rho^{-1}
       =\begin{pmatrix}1+d_N&q_N/(N\rho)\\N\rho d_N&q_N\end{pmatrix}.
 \tag{13}
\]
Use a fixed-width complex neighborhood in \(y\) of
\[
       [1/2,\,1/(2\rho)-1/2],
 \tag{14}
\]
with that width chosen small, for instance less than \(1/16\).
In the corresponding \(x\)-domain the distances from \(0\) and
\(1/2\) are at least a constant times \(\rho\). Increasing \(M\)
in (5), all shifted sine denominators in (10) stay away from
their zeros on this domain.

Uniformly on a slightly larger such domain and on a larger
bounded parameter disk,
\[
 |q_N-1|\le\frac{C}{N\rho},\qquad
 |d_N|\le\frac{C}{N^2\rho^2},\qquad
            \|\widetilde T_N-I_2\|\le C\epsilon.
 \tag{15}
\]
Here is a direct uniform justification. The exact quotient is
\[
 q_N(x)=
 \left(\frac{\sin\pi x}{\sin(\pi x+\pi/N)}\right)^4
                 \frac{\sin(2\pi x+2\pi/N)}{\sin(2\pi x)}.
 \tag{16}
\]
Each shift is \(O(N^{-1})\), while the logarithmic derivatives
of these sine factors are \(O(\rho^{-1})\) on the enlarged
domain. Their ratios differ from one by \(O((N\rho)^{-1})\).
Also \(|c(0)-w_N|\le C_A N^{-2}\), and
\[
                 |A_N(Nx)^{-1}|\le C\rho^{-2}.
 \tag{17}
\]
For (17), near zero the numerator of this reciprocal has two
factors of size \(O(|x|+N^{-1})\) and the denominator four
factors comparable to \(|x|+N^{-1}\). Away from zero the
denominator is uniformly bounded below. Near \(x=1/2\) its
numerator becomes small, so the reciprocal decreases. On the stated
complex domain these comparisons are uniform. This proves
(15). Cauchy's formula in the fixed \(y\)-width gives
\(\|\partial_y\widetilde T_N\|\le C\epsilon\) on a smaller
width, with the same assertion for any fixed derivatives.

The rescaled actual state
\[
           \mathcal Z_j=(S_\rho X_j,\,\rho S_\rho Y_j)^t
 \tag{18}
\]
therefore has exact step
\[
 \mathcal Z_{j+1}=\widetilde{\mathbb T}_N(j/(N\rho))\mathcal Z_j,
 \qquad
 \widetilde{\mathbb T}_N=
 \begin{pmatrix}
 \widetilde T_N&0\\
 \partial_y\widetilde T_N&\widetilde T_N
 \end{pmatrix}
                    =I_4+O(\epsilon).
 \tag{19}
\]
This explains the extra factor \(\rho\) on the normal block.
The third component is exactly \(\rho c_N'(j/N)G_j\).

The endpoint-product source proves a polynomial real spectral
norm for \(K_N\), uniformly on every bounded complex parameter
disk. Markov's inequality then bounds its first normal by another
fixed power of \(N\). Consequently
\[
                         |\mathcal Z_j|\le C_A N^{p_A}
 \tag{20}
\]
on the whole buffered node interval in (14). The factors
\(\rho,\rho^2\) in (18) do not increase this bound.
No propagation over an interval of length \(1/\rho\) is used to
obtain (20).

## 3. Long-domain interpolation costs only polynomial factors

We spell out how the proof of the fixed-interval two-channel
theorem applies to (19). This avoids hiding a buffer-dependent
exponential constant in an invocation of that theorem.

In the \(y\)-coordinate the step is \(\epsilon\), the analytic
width and the constant in \(I_4+O(\epsilon)\) are fixed. Choose
fixed local disk and block lengths as in that proof. Its nested
Cauchy estimate for the exact matrix finite differences is
\[
                         \|B_k\|\le C_0^k k!
                    \qquad(k\epsilon\le c_0),
 \tag{21}
\]
with \(C_0,c_0\) independent of \(\rho,N\). A Newton polynomial
of degree \(\lfloor\ell/\epsilon\rfloor\), with a sufficiently
small fixed \(\ell>0\), therefore matches its node block exactly
and has norm \(CM_N\) on a fixed larger disk, where
\(M_N=C_A N^{p_A}\) from (20).
Adjacent blocks have at least \(c/\epsilon\) common nodes.
The disk Blaschke estimate gives overlap error
\[
                             CM_Ne^{-c_1/\epsilon}.
 \tag{22}
\]
The constants are uniform along the long interval (14).

There are \(O(\rho^{-1})\) blocks. Use the same fixed smooth
transition cutoffs as in the source, with bounded overlap.
The resulting smooth function has norm \(CM_N\), and its
\(\bar\partial\) has norm bounded by (22). Cut that density
off in the fixed-width long rectangle and take its plane
Cauchy transform. Its support has area \(O(\rho^{-1})\).
For every point of the plane,
\[
 \int_{\rm support}\frac{dA(\zeta)}{|y-\zeta|}
       \le 2\pi+\operatorname{area}(\rm support)
       \le C\rho^{-1}.
 \tag{23}
\]
The first term bounds the unit disk, and outside it the kernel
is at most one. Thus the Cauchy correction is at most
\[
                         CM_N\rho^{-1}e^{-c_1N\rho}.
 \tag{24}
\]
Neither the number of blocks nor the Cauchy operator has an
exponential cost in \(1/\rho\).

There are \(O(N)\) original nodes in the long interval. Repair
their errors by the exact finite sinc interpolation of the source,
whose cardinal factors are
\(\operatorname{sinc}(y/\epsilon-j)=\operatorname{sinc}(Nx-j)\).
On a fixed sufficiently narrow \(y\)-strip the repair has bound
\[
             CNM_N\rho^{-1}
                     e^{-c_1N\rho+\pi N\rho|\Im y|}.
 \tag{25}
\]
Choose that width less than \(c_1/(4\pi)\). The final interpolated
four-vector is exact at every node in a buffered interval
containing \(I_\rho\), is jointly holomorphic, and has polynomial
norm \(CN^{p_A+1}\rho^{-1}\). This conclusion holds even when
\(N\rho\) is merely bounded below by the sufficiently large \(M\);
in that case the asserted exponential improvement can be small,
but the norm bound remains polynomial.

Its first component is \(f_N\). Divide its third component by
\(\rho c_N'(x)\) to obtain \(\mathcal G_N\). In this domain
\[
                       |\rho c_N'(x)|\ge c\rho^2,
 \tag{26}
\]
so this division costs only \(\rho^{-2}\). We have proved
polynomially bounded exact separate channels on a common
\(x\)-neighborhood of width \(r_1\rho\), for some \(r_1>0\).
They are available on a buffered real interval slightly larger
than \(I_\rho\). All integrations, cutoffs and repair nodes are
independent of \(\alpha\), preserving its holomorphic dependence.

## 4. A uniform exact high-normal amplitude near the endpoint

Use the exact finite lowering amplitude \(\Gamma_N^\delta\) from
the scalar-compatibility source. Its ratios and base are
\[
 \rho_{\ell,N}(\alpha,t)=
 \frac{[\cos^2 A_\ell+\sinh^2(\alpha/(2N))]
        [\sin^2(t/2)-\sin^2 A_\ell]}{\cos^4B_\ell},
 \qquad
 \Gamma_N^\delta=T_{0,N}\sum_{l=0}^{\lfloor\delta N\rfloor}
                                      \prod_{\ell<l}\rho_{\ell,N},
 \tag{27}
\]
where \(B_\ell=A_\ell+\theta/2\), and
\(A_\ell=(\ell+1/2)\theta\) at even levels or
\((\ell+1)\theta\) at odd levels. The exact bases are
\[
 T_{0,N}=
 \begin{cases}
 N^{-1}\cosh(\alpha/2)\sin t,&N\text{ even},\\
 \displaystyle
 \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
 {N\cos^4(\theta/2)}\sin t\sin(t/2),&N\text{ odd}.
 \end{cases}
 \tag{28}
\]
No infinite extension of this finite sum is used.

Consider a small positive center \(u\), with \(Nu\ge M\), and a
relative disk \(|x-u|\le\varepsilon_0u\). Set
\[
 \delta=\frac12-\frac9{10}u,\quad L=\lfloor\delta N\rfloor,\quad
 t=\pi-2\pi x-\pi/N,\quad
 v=\sin^2\!\left(\pi x+\frac{\pi}{2N}\right),\quad
 v_\delta=\sin^2(9\pi u/10).
 \tag{29}
\]
There are absolute \(u_0,\varepsilon_0>0\), and a sufficiently
large \(M\), such that throughout \(0<u\le u_0\),
\[
                         |v-v_\delta|\le\tfrac12v_\delta.
 \tag{30}
\]
For completeness this is a uniform scaled continuity statement:
divide both \(v\) and \(v_\delta\) by \(u^2\). The expressions
extend continuously to \(u=0\), with variables \(x/u\) near one
and \(1/(Nu)\) near zero. Their ratio at the limiting center is
\(100/81\), strictly inside the disk of radius \(1/2\) about one.
Choose \(\varepsilon_0\) and \(1/M\) small, then \(u_0\) small,
to retain that strict inequality. These choices are independent
of \(N,u,\alpha\).

For all factors used in (27),
\(\cos^2A_\ell\ge v_\delta\). Equation (30) implies
\[
 \left|1-\frac{v}{\cos^2A_\ell}\right|\le1.
 \tag{31}
\]
Indeed the disk of radius \(v_\delta/2\) about \(v_\delta\) lies
inside every disk of radius \(U\) about \(U\ge v_\delta\).
Since \(\sin^2(t/2)=1-v\), (31) is exactly the bound for the
limiting factor in (27).

The finite ratio itself need not be uniformly below one.
Instead apply the product comparison
\[
 \left|\prod_{\ell<l}\rho_{\ell,N}\right|
 \le
 \left(\prod_{\ell<l}\frac{\cos A_\ell}{\cos B_\ell}\right)^4
 \prod_{\ell<l}
       \left(1+\frac{C_A}{N^2\cos^2A_\ell}\right).
 \tag{32}
\]
The disjoint intervals \([A_\ell,B_\ell]\) give
\[
 \prod_{\ell<l}\frac{\cos A_\ell}{\cos B_\ell}
                          \le\frac1{\cos B_{l-1}}\le C/u.
 \tag{33}
\]
The last inequality uses
\(\pi/2-B_{l-1}\ge9\pi u/10-\pi/(2N)\ge cu\).
For a nonempty product all angles also remain at distance at
least \(3\theta/2\) from \(\pi/2\), after enlarging \(M\).
Their distances increase backwards in steps of \(\theta\).
The reciprocal-square estimate from the outer-row proof is
therefore uniform:
\[
                       \sum_{\ell<l}\sec^2 A_\ell\le CN^2.
 \tag{34}
\]
The last product in (32) is at most \(e^{C_A}\).
Since \(|T_{0,N}|\le C_Au/N\) and there are at most \(N\)
summands,
\[
                      |\Gamma_N^\delta(\alpha,t)|\le C_Au^{-3}.
 \tag{35}
\]
This is a polynomial bound on a complex relative disk. It has
no requirement that \(Nu^2\) tend to infinity.

The interpolation is still exact at every physical node in a
slightly smaller relative disk. Its lowering stop is
\(p_j=\lfloor N/2\rfloor-1-j\). For \(j/N\) near \(u\),
\[
                        L-p_j\ge cNu
 \tag{36}
\]
after enlarging \(M\), because \(9/10<1-\varepsilon_0\).
Thus the finite sum includes the actual stop, and every later
product vanishes exactly. This verifies physical termination
with uniform margins rather than invoking a fixed-cutoff limit.

Near \(x=1/2\), the angle \(t\) is near zero. Use the fixed
cutoff \(\delta=1/8\) instead. Its contraction domain contains
a fixed neighborhood of zero, so \(\Gamma_N^\delta=O_A(N^{-1})\)
and exact termination hold there, also on relative endpoint
disks. The remaining middle compact interval is covered by
finitely many fixed charts from the scalar-compatibility theorem.
Consequently every point of \(I_\rho\) has a disk of radius at
least \(c\rho\) on which the actual high normal has an exact
analytic amplitude with norm at most \(C_A\rho^{-3}\).
Fixed derivatives on smaller disks cost only powers of \(\rho^{-1}\).

## 5. Uniform quotient and checkerboard cancellation

Let \(L_N(Z,\alpha)\) be the ordinary low interpolation at all
distinct physical nodes, and let \(\mathcal P_N\) be the monic
distinct-root polynomial. The exact formulas are
\[
 \mathcal P_N(c_N(x))=-a_N(x)\sin(\pi Nx),\qquad
 a_N(x)=
 \begin{cases}
 2,&N\text{ even},\\
 4\cos(\pi x+\pi/(2N)),&N\text{ odd}.
 \end{cases}
 \tag{37}
\]
On the buffered shrinking domain \(|a_N|\ge c\rho\).
The low interpolant has polynomial real norm, uniformly for
bounded complex \(\alpha\), and degree \(J=\lfloor(N-1)/2\rfloor\).
Hence
\[
              |L_N(c_N(x),\alpha)|\le CN^p
                                  e^{2\pi J|\Im x|},\quad 2J<N.
 \tag{38}
\]
On a rectangle of height \(c_2\rho\) around \(I_\rho\), move
the vertical sides to half-grid positions within its fixed
relative buffers. For sufficiently large \(M\) this is possible.
The sine denominator in (37) is bounded below by
\(\frac12e^{\pi N|\Im x|}\) on those sides and by
\(c e^{\pi Nc_2\rho}\) on the horizontal sides.

The numerator of
\[
                  g_N(x,\alpha)=
        \frac{L_N(c_N(x),\alpha)-f_N(x,\alpha)}
                              {\mathcal P_N(c_N(x))}
 \tag{39}
\]
vanishes at every denominator grid zero in the rectangle.
The quotients are removable jointly in \(\alpha\).
Equations (37)--(38), the bound from Section 3, and the maximum
principle give \(\|g_N\|\le CN^P\rho^{-P}\) there. In particular
the constant in this quotient estimate has only polynomial
dependence on the buffer.

Write \(\nu_N(x)=2\pi x+\pi/N\) and \(\tau_N(x)=\pi-\nu_N(x)\).
On each chart of Section 4 the exact actual nodal defect is
\[
 \Delta_{j,N}=c_N'(j/N)G_j-f_N'(j/N)
                  =(-1)^j\mathcal A_N^\delta(j/N,\alpha),
\]
\[
 \mathcal A_N^\delta
   =-\pi Na_Ng_N
       -\frac{\pi\Gamma_N^\delta(\alpha,\tau_N(x))}
                    {\sin\nu_N(x)}.
 \tag{40}
\]
This is the exact both-parity normal calculation in the scalar
compatibility source. The sine denominator has modulus at least
\(c\rho\). Therefore \(\mathcal A_N^\delta\) is polynomially
bounded in \(N,\rho^{-1}\), as is
\[
                       \mathfrak d_N=c_N'\mathcal G_N-f_N'.
 \tag{41}
\]

Take a disk of radius \(R=c_3\rho\) about any real point of
\(I_\rho\), within all the required domains. Its central interval
contains at least \(c_4N\rho\) even grid indices and that many odd
indices, by increasing \(M\). The functions
\(\mathfrak d_N-\mathcal A_N^\delta\) and
\(\mathfrak d_N+\mathcal A_N^\delta\) vanish respectively on those subgrids.
The disk Blaschke argument from the fixed-buffer proof gives
one uniform factor less than one per zero. Thus, on a smaller disk,
\[
                     |\mathfrak d_N|+|\mathcal A_N^\delta|
                         \le CN^P\rho^{-P}e^{-c_5N\rho}.
 \tag{42}
\]
Covering \(I_\rho\) by these disks gives the same estimate on
a common neighborhood of width \(c_6\rho\). Taking a supremum
over the cover adds no exponential cost. Cauchy estimates give
the derivative assertions after a further fixed relative shrink.

## 6. Exact repair, shrinking scales, and the remaining currents

Use the actual \(\Delta_{j,N}\) from (40) and set
\[
 h_N(x,\alpha)=f_N(x,\alpha)+
 \sum_{j:\,j/N\in I_\rho}
       \Delta_{j,N}(\alpha)(x-j/N)\operatorname{sinc}^2(Nx-j).
 \tag{43}
\]
Its values and first derivatives give (9) exactly. There are
at most \(N\) terms, and the correction is bounded by
\[
                    CN^{P+1}\rho^{-P}
                    e^{-c_5N\rho+2\pi N|\Im x|}.
 \tag{44}
\]
Choose the final width \(r\rho\) with \(r<c_5/(4\pi)\), also
inside the previous domains. Equations (42)--(44) prove (7)--(8),
after increasing \(P\). The proof used enlarged parameter disks,
so all claimed holomorphic derivatives follow. This completes
Theorem 1.

For \(0<\kappa<1\), choose
\(\rho=N^{-1+\kappa}\), or a fixed constant multiple of it.
The true normal defect and scalar repair are then
\[
                  \operatorname{poly}(N)e^{-cN^\kappa},
 \tag{45}
\]
on a strip of width \(c'N^{-1+\kappa}\), throughout the interval
from index \(N^\kappa\) to within \(N^\kappa\) of the other
endpoint. Choosing a smaller fixed multiple of the buffer places
an index \(j=\lfloor N^\kappa\rfloor\) strictly inside this overlap.
This statement concerns the actual values and spectral normals;
it assumes no limiting endpoint profile.

At \(\rho=K\log N/N\), the same proof gives any prescribed
negative power of \(N\) in (8) by taking a sufficiently large
fixed \(K\). Indeed \(\rho^{-P}\le N^P\) and the exponential
factor is \(N^{-cK}\), while \(P,c\) are independent of \(K\).
For bounded \(N\rho\), the theorem still supplies exact
interpolation and a polynomial norm, but it does not claim
smallness of the error in (8).

The map \(c_N\) is one-to-one on the final shrinking rectangle,
with \(|c_N'|\ge c\rho\). The cosine alternatives
\(x-y\in\mathbb Z\) and \(x+y+1/N\in\mathbb Z\) prove this:
the second is excluded by \(N\rho\ge M\) and the relative buffers.
Thus (43) is a genuine local spectral Hermite representative.
Fixed products preserve shared values and normals by the ordinary
product rule, with only changed polynomial exponents. Other graph
factors and all their remaining traces stay untouched.

There is a precise distinction from two existing global estimates.
First, the full-period Hermite obstruction gives for real bounded
\(\alpha\) a norm at least
\[
      c_A N^{-2}\frac{(1-e^{-NH})^2}{2\cosh H}\,e^{NH}
 \tag{46}
\]
for an even periodic representative with *all* physical data on
a strip of height \(H\). At \(H\asymp N^{-1+\kappa}\) this is
superpolynomial. Our rectangles omit the two endpoint buffers
and impose no periodic identification. They cannot simply be
closed into that periodic strip with the same polynomial bound.

Second, the omitted high-row estimate for a fixed cutoff is
\[
 |\omega_{j,N,L}|\le CN^4
            \exp[-\delta\pi^2(j+1/2)^2/N].
 \tag{47}
\]
At \(j=N^\kappa\) with \(\kappa<1/2\), this upper estimate provides
no small exponential penalty. Exact scalar overlap (45) therefore
does not discard those original endpoint rows. It also does not
bound their attached physical kernels or coherent remaining trace.

In a window-contour formula the new width permits heights
\(H=O(\rho)\), but the two external vertical currents remain
exactly present. Their kernel is concentrated within \(O(N^{-1})\)
of the real axis, so shrinking the permitted height alone is not
a cancellation argument. A splice to an endpoint representation
must retain the oriented interface and the original joint spectator.
No whole-current action estimate or nonzero scalar coefficient
is inferred here.

## 7. Direct source readbacks and coverage

The fixed-buffer scalar theorem and its separate-channel input did
not quantify their domains as the physical endpoints moved.
The additions here are the uniform rescaled recurrence, polynomial
long-domain gluing cost, and the exact complex lowering-product
bound (32)--(35). Together these yield the \(N\rho\) exponential
scale without a condition on \(N\rho^2\).

The following complete source texts were read at these unchanged
versions, their directly used implications checked, and their hashes
verified:

* [Actual two-channel interpolation](research_microscopic_endpoint_two_channel_interpolation.md),
  SHA256 44f6db0f8afdf1205ab8b0935b95b8a4fd9fa16c6414be2467b8b40a123c0ffe:
  original prolonged recurrence and the local Newton, Cauchy-gluing
  and sinc construction, with constants tracked in Section 3.
* [Actual omitted endpoint rows](research_endpoint_outer_row_decay.md),
  SHA256 85e708606a44cbbbc45a82db0685fcb1d35215c89470ccdc7408790305e55e30:
  exact finite lowering factors, cosine-product and reciprocal-square
  estimates, and the original physical-row penalty (47).
* [Fixed-buffer scalar compatibility](research_microscopic_endpoint_bulk_scalar_compatibility.md),
  SHA256 2b8713ed16b66f5faa004403ac1d032021eee0a6f8f38082481d002c672c0b2e:
  distinct-root quotient, exact normal sign, local physical
  termination, dense parity subgrids, and scalar Hermite repair.
* [Endpoint-product polynomial bounds](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  full physical kernel and low-interpolant polynomial bounds on
  every bounded complex microscopic parameter disk.
* [Full-period Hermite strip obstruction](research_endpoint_periodic_hermite_strip_obstruction.md),
  SHA256 c59ddd8157a1ad9c9478cec6014fe25d35afbeab4b312fb6e7309fb627b39ea5:
  the quantitative restriction (46), with its full-period hypothesis.

Only written mathematics, source-text reads, and hashes were used.
No mathematical program, numerical experiment, test, or build was
run. Adopted notes and public manuscripts remain unchanged.
