# A polynomial-cost canonical lift of the actual averaged co-source

Private written proof, 18 November 2026.

The original one-cell averaged row has an exact lift through the
canonical finite Hermite kernel. The input remains the actual
unreduced boundary function. Only the output is replaced by its full
Hermite representative. The lift costs at most a fixed polynomial in
the level, measured against the input's supremum on the real physical
interval; no derivative of that input enters the bound.

The complete proof directs are **A**, the actual averaged filling
row; **K**, the canonical Hermite kernel split; and **F**, the actual
Fourier--Hermite interpolation. Their complete pins appear below.

## 1. Actual row, raw average and output interpolation

Fix \(N\ge2\), a signed integer \(n\), and
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad
 h=\frac{2\pi i}{N},\qquad a=\frac{2\pi}{N},\qquad
 \eta=(-1)^d,\qquad b_n=1+\frac{|n|}{2}.
 \tag{1}
\]
Use the physical algebra, circle basis and crossing of K:
\[
 \mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 L_j=(-1)^{j-1}U_{j-1}(z/2),\qquad
 \left\|\sum_{j=1}^N c_jL_j\right\|_\circ=\sum_j|c_j|,
 \tag{2}
\]
\[
 \phi_n(F)=\phi(R^nF),\qquad
 \phi(F)=\eta N^2[z^d](F\bmod(2T_N(z/2)+2)).
 \tag{3}
\]
Every double-root normal and the odd-level simple-root value remain
in this quotient. Negative \(n\) means the actual inverse crossing.

Let \(G(t)\) be even and holomorphic on a symmetric neighborhood of
\([-\pi,\pi]\). Every actual unreduced polynomial \(P(z)\) is included
by taking \(G(t)=P(-2\cos t)\). More generally the same is true for
\(P\) holomorphic near \([-2,2]\). Put
\[
 M_G=\sup_{t\in[-\pi,\pi]}|G(t)|,\qquad z(t)=-2\cos t,
\]
\[
 f(t)=q^{nd^2/4}e^{-nt^2/(2h)},\qquad
 w(t)=\sin t\,f(t),\qquad g(t)=w(t)G(t).
 \tag{4}
\]
The phase in (4) is the displayed physical lift. For real \(t\),
\(|f(t)|=1\), including negative \(n\). The raw average is
\[
 A_G(t)=\frac1a\int_{t-a/2}^{t+a/2}g(v)\,dv,\qquad
 k_G(t)=\frac{A_G(t)}{w(t)}.
 \tag{5}
\]
Near real integration segments the integral is holomorphic in \(t\).
This follows by using a common holomorphic primitive of \(g\) on a
thin simply connected neighborhood of the segment. The function
\(g\) is odd, so \(A_G\) is odd and \(k_G\) is even wherever defined.
The zero of \(w\) at zero is simple. Thus \(k_G\) extends evenly and
holomorphically through zero, and is holomorphic in \(z+2\) there.

The physical midpoints are
\[
 t_j=-\pi+(j+\tfrac12)a,\qquad 0\le j<N.
 \tag{6}
\]
Their nonzero sine values give ordinary holomorphic \(z\)-germs.
Evenness makes the germs at \(t_j\) and \(-t_j\) compatible, including
the first \(z\)-derivative at a double root. Let
\[
 \mathcal J_N k_G\in\mathcal H_N
 \tag{7}
\]
be their unique full Hermite representative. At odd \(N\), the
midpoint zero supplies only the simple-root value. No derivative in
\(z\) is imposed there.

The notation \(\mathcal J_N\mathcal K_{N,n}G\) will also denote (7),
where \(\mathcal K_{N,n}\) is the actual raw operation (5).
This definition never first replaces \(G\) by a quotient
representative: the integral uses its original intermediate values.

## 2. Nodal bounds from cell endpoints alone

The exact derivative identity is
\[
 A_G'(t)=\frac{g(t+a/2)-g(t-a/2)}a.
 \tag{8}
\]
All real cells centered at (6) lie in \([-\pi,\pi]\). Hence
\[
 |A_G(t_j)|\le M_G,\qquad
 |A_G'(t_j)|\le \frac{N}{\pi}M_G.
 \tag{9}
\]
At a nonzero midpoint,
\[
 |\sin t_j|\ge\sin(\pi/N)\ge\frac2N,\qquad
 \left|\frac{w'(t_j)}{w(t_j)}\right|
 =\left|\cot t_j-\frac{nt_j}{h}\right|
 \le\frac{(1+|n|)N}{2}.
 \tag{10}
\]
For odd \(N\), the nearest nonzero midpoint to zero has distance
\(2\pi/N\); the endpoint midpoints still give the minimum in (10).
The assertion also includes \(N=2\).

Differentiating the quotient in (5), and using (8) rather than
differentiating \(G\), gives
\[
 |k_G(t_j)|\le\frac N2M_G,\qquad
 |k_G'(t_j)|
 \le c_nN^2M_G,\qquad
 c_n=\frac1{2\pi}+\frac{1+|n|}{4}.
 \tag{11}
\]
At the odd simple midpoint, oddness and (8) instead give
\[
 k_G(0)=\frac{2g(a/2)}{a f(0)},\qquad
 |k_G(0)|\le \frac{2\sin(a/2)}a M_G\le M_G,\qquad
 k_G'(0)=0.
 \tag{12}
\]
Consequently the bounds (11) hold at every midpoint when the last
zero derivative is used at the simple node. The derivative bound is
for the logarithmic circle coordinate; it has not been obtained by
dividing by a small Casimir-node separation.

## 3. Full Fourier recovery and its norm

For completeness the relevant alias inverse from F can be applied
directly to these arbitrary compatible output germs. Put
\[
 \omega_j=q^{2j+1}=-e^{it_j},\qquad
 h_j=k_G(t_j),\qquad d_j=-i k_G'(t_j),
\]
\[
 H_\ell=\frac1N\sum_jh_j\omega_j^{-\ell},\qquad
 D_\ell=\frac1N\sum_jd_j\omega_j^{-\ell},
 \qquad 0\le\ell<N.
 \tag{13}
\]
If the canonical representative is written as
\[
 P(z)=a_0+\sum_{\ell=1}^{N-1}a_\ell\,2T_\ell(z/2),
 \tag{14}
\]
then \(P(\omega+\omega^{-1})\) has coefficients \(a_\ell\) at
the positive and negative Laurent exponents. Since
\(\omega_j^N=-1\), its value and logarithmic-derivative aliases are
\[
 H_\ell=a_\ell-a_{N-\ell},\qquad
 D_\ell=\ell a_\ell+(N-\ell)a_{N-\ell},
 \qquad 1\le\ell<N.
 \tag{15}
\]
Here \(\omega\partial_\omega=-i\partial_t\), explaining exactly
the sign in (13). The paired values agree and the paired
derivatives are opposite; at the odd fixed node the derivative is
zero. Therefore the alias system has precisely the required
Hermite compatibility, including the even middle alias. It yields
\[
 a_0=H_0,\qquad
 a_\ell=\frac{D_\ell+(N-\ell)H_\ell}{N}.
 \tag{16}
\]
Equations (11)--(12) imply
\[
 |a_0|\le \frac N2M_G,\qquad
 |a_\ell|\le(c_n+\tfrac12)NM_G\le b_nNM_G.
 \tag{17}
\]
The last inequality follows from \(1/(2\pi)\le1/4\).
Set \(a_N=a_{N+1}=0\). The second-kind coefficients are exactly
\(\beta_j=(-1)^j(a_j-a_{j+2})\), \(0\le j<N\), since
\(2T_\ell=U_\ell-U_{\ell-2}\), with the usual endpoint convention.
Thus
\[
 \boxed{\quad
 \|\mathcal J_N\mathcal K_{N,n}G\|_\circ
       \le 2\sum_{\ell=0}^{N-1}|a_\ell|
       \le 2b_nN^2M_G .
 \quad}
 \tag{18}
\]
Only real-interval values of the input occur in this estimate.
Its degree, complex-neighborhood size and derivatives do not enter.
Holomorphy supplies the actual nodal germs, not an additional
quantitative derivative hypothesis.

## 4. Exact canonical lift and the original closing row

K supplies the endomorphism and its specified inverse off the
period line,
\[
 \widetilde K_n=M_{R^{-n}}K_0M_{R^n},\qquad
 G_n=M_{R^{-n}}G_0M_{R^n},\qquad
 \widetilde K_nG_n=I-P_n,
\]
\[
 P_nF=u_n\phi_n(F),\qquad
 u_n=R^{-n}L_N/N^2,\qquad
 \|G_n\|_\circ\le18\pi N^5b_n^2.
 \tag{19}
\]
The exact row from A, valid for compatible nodal germs, is
\[
 \frac{\phi_n(\mathcal J_N k_G)}{\eta N^2}
 =\frac1{N^2}\sum_{j=0}^{N-1}[w(t)k_G(t)]'_{t=t_j}.
 \tag{20}
\]
Its right side telescopes by (8):
\[
 \frac{\phi_n(\mathcal J_N k_G)}{\eta N^2}
 =\frac{g(\pi)-g(-\pi)}{N^2a}=0.
 \tag{21}
\]
Both endpoints are present. Their sine factors vanish and the two
input endpoint values are finite. The proof uses neither periodicity of the Gaussian nor
an identification of its off-grid branches.

Define the linear map from the recorded analytic inputs to the
physical finite algebra by
\[
                 \mathcal Q_{N,n}G
                    =G_n\mathcal J_N\mathcal K_{N,n}G .
 \tag{22}
\]
Equations (18)--(21) prove the complete lift identity and norm:
\[
 \boxed{\quad
 \widetilde K_n\mathcal Q_{N,n}G
       =\mathcal J_N\mathcal K_{N,n}G,\qquad
 \phi_n(\mathcal Q_{N,n}G)=0,\qquad
 \|\mathcal Q_{N,n}G\|_\circ
       \le36\pi b_n^3N^7M_G .
 \quad}
 \tag{23}
\]
Indeed \(P_n\mathcal J_N k_G=0\), and \(G_n\) maps
\(\ker\phi_n\) into itself. The lift in (22) is the unique one
in that kernel, since \(\widetilde K_n\) is invertible there.
In particular, for any original boundary class \(H\) and any
such recorded \(G\),
\[
 \phi_n\bigl(H-\widetilde K_n\mathcal Q_{N,n}G\bigr)
                         =\phi_n(H).
 \tag{24}
\]
An actual unreduced short-boundary polynomial may itself be used
as \(G\), without any degree restriction. Spectator variables and
the other prescribed contractions are retained by linearity.
For a holomorphic parameter family, the construction is
holomorphic in those parameters and the estimates are uniform
where their real-interval suprema are uniform.

## 5. A bounded reverse map and the exact co-source image

The image in (21) is the entire kernel, not merely a subspace of it.
For \(F\in\ker\phi_n\), let \(p\) be the canonical polynomial
representing \(R^nF\), and put
\[
 H=G_0p,\qquad
 (\mathcal S_{N,n}F)(t)=f(t)^{-1}H(-2\cos t).
 \tag{25}
\]
Here \(G_0\) is K's zero-twist inverse. Since \(\phi(p)=0\),
\(K_0H=p\). The input in (25) is entire and even in \(t\).
It is not required to descend holomorphically to \(z\) at \(z=2\).
This is why the recorded analytic input class includes even
angle functions, rather than only functions holomorphic on a
complex neighborhood of the closed Casimir interval.

The same scalar \(f\) occurs in (4) and (25). It cancels exactly
inside the raw numerator:
\[
 \mathcal K_{N,n}(\mathcal S_{N,n}F)(t)
   =f(t)^{-1}\frac1{\sin t}
       \int_{-1/2}^{1/2}
       \sin(t+a\rho)H(z(t+a\rho))\,d\rho
   =f(t)^{-1}p(z(t)).
 \tag{26}
\]
The zero-twist polynomial identity holds also at zero by
removability. A proves that the full required nodal jets of \(f\)
are those of \(R^n\). They are nonzero, so inversion and
multiplication preserve those jets. Consequently
\[
 \boxed{\quad
 \mathcal J_N\mathcal K_{N,n}\mathcal S_{N,n}F
       =R^{-n}p=F,\qquad F\in\ker\phi_n.
 \quad}
 \tag{27}
\]
This is an identity of the full Hermite classes, not only their
values at distinct roots.

For real \(t\), the elementary identity
\(\sin(jt)/\sin t=\sum_{\ell=0}^{j-1}e^{i(j-1-2\ell)t}\)
gives \(|L_j(-2\cos t)|\le j\le N\), including endpoints.
Using K's estimates for \(G_0\) and \(M_{R^n}\), one obtains
\[
 \boxed{\quad
 \|\mathcal S_{N,n}F\|_{[-\pi,\pi]}
 \le N\|G_0p\|_\circ
 \le \frac{\pi N^2}{2}\|R^nF\|_\circ
 \le 3\pi b_nN^4\|F\|_\circ .
 \quad}
 \tag{28}
\]
The Gaussian inverse has modulus one only on the real interval;
no analogous uniform bound on a fixed complex strip is asserted.

There is also an exact, qualitative polynomial-image conclusion:
\[
 \operatorname{im}\bigl(
   P(z)\longmapsto\mathcal J_N\mathcal K_{N,n}
                          [P(-2\cos t)]\bigr)=\ker\phi_n.
 \tag{29}
\]
To prove it, every continuous even function on \([-\pi,\pi]\)
is a continuous function of \(z=-2\cos t\). Such a function is
uniformly approximated by polynomials in \(z\). An elementary
proof after rescaling to \([0,1]\) uses its Bernstein polynomials:
the binomial weights have total mass one, mean \(x\), and variance
\(x(1-x)/m\). Uniform continuity controls weights within distance
\(\varepsilon\), and their total mass outside that distance is at
most \(1/(4m\varepsilon^2)\). This proves uniform convergence.
Apply this to (25). Formula (18), applied to the difference with
each polynomial, shows convergence of the output to \(F\).
The polynomial output image is a linear subspace of the
finite-dimensional space \(\mathcal H_N\), hence closed.
Together with (21), this proves (29).
No bound on the degree of the resulting exact polynomial input
is extracted by this argument. The explicitly bounded reverse
map is (25).

Thus the co-source quotient of the physical finite vector space
is exactly one-dimensional and is identified by its original row
\(\phi_n\). This statement is about vector spaces, not ideals or
a thimble or Gauss--Manin local system.

## 6. Retained block currents and the limit of the result

For a consecutive proper block \(j=r,\ldots,s\), define its normalized
Hermite row by the corresponding subsum of (20). The same full-output
representative, or equivalently \(\widetilde K_n\mathcal Q_{N,n}G\),
satisfies the exact identity
\[
 \frac1{N^2}\sum_{j=r}^{s}[wk_G]'(t_j)
   =\frac{g(t_s+a/2)-g(t_r-a/2)}{N^2a}.
 \tag{30}
\]
For physical unnormalized trace currents multiply by \(\eta N^2\).
The canonical lift has therefore preserved the two block endpoints;
it has not turned a proper portion of the row into a zero row.

The polynomial bound (23) connects two operations already acting on
the same original source: raw averaging followed by full output
interpolation, and a finite kernel coboundary. It does not identify
raw averaging with \(\widetilde K_n\) between grid points. The input
to raw averaging can have arbitrary high degree, and replacing it
before averaging is not part of the theorem. Possible poles of the
raw quotient at \(t=\pm\pi\) are irrelevant to the nodal construction;
no uniform holomorphic bound at those endpoints has been asserted.

In particular, this lift alone does not construct a complex-domain
parametrix or a contour deformation. It does not bound the unknown
remaining coordinate \(u_n\phi_n(H)\) by a geometric volume, nor
select a geometric coefficient. Any such localization must still
construct its actual input \(G\), retain (30) on partial domains,
and control the other source boundaries and aliases.

## Complete proof-source pins

* A: notes/research_averaged_hermite_regular_filling_row.md, SHA256
  c25a038a8cf585dd7d0a07de9baf7f8a379b669739dc865d110976fca86e696a.
* K: notes/research_canonical_hermite_filling_kernel_split.md, SHA256
  bf615d1dcf2193b1c277599c2730ab3e1da01001b7e42927c77c5cbe044a74e6.
* F: notes/actual_twist_circle_fourier_kernel.md, SHA256
  1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292.

A supplies the literal Gaussian lift, full Hermite closing row and
raw cell operation. K supplies the canonical kernel and its complete
inverse estimate. F supplies the alias interpolation scheme, whose
application to arbitrary compatible output germs was proved inline.
Only written mathematics and text/hash operations were used.
Frozen notes and public manuscripts are unchanged.
