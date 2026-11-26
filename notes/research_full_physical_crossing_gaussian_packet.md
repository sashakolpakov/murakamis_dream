# A whole physical Gaussian packet for one original crossing

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The original signed crossing, in the uniform physical head metric, has
a Gaussian approximation in the Hilbert--Schmidt norm of its entire
matrix. Every fixed number of correction terms is available. The estimate
is uniform for small real exponential boundary tilts and retains the
exact physical phase. It strengthens the weighted norm rate of [W];
it does not identify a geometric tilt or control a closed knot scalar.

## 1. The actual entry, phase, and boundary tilts

Put \(q=e^{\pi i/N}\), \(Q=q^2\), \(d=N-1\), \(x=-q^{-1}\),
\(\kappa=q^{d^2/2}\), and
\[
 F_j=(Q;Q)_j,\qquad
 s_j=\prod_{h=1}^j2\sin(\pi h/N),\qquad F_0=s_0=1.
 \tag{1}
\]
Fractional powers mean the displayed exponentials. Declare the actual
balanced basis \(w_0,\ldots,w_d\) orthonormal, as in [P], and use the
unnormalized matrix Hilbert--Schmidt norm on its physical pair.

The checked positive crossing sends input \((a,b)\) to
\((b+k,a-k)\), with \(0\le k\le a\), \(b+k\le d\).
There is one summand for this entry. Set \(j=a-k\). Directly from
[B, (2)] and its Cartan diagonal, its full coefficient is
\[
 R^+_{(b+k,j);(j+k,b)}
 =\kappa x^{-b-j}Q^{jb}
           \frac{F_{b+k}F_{j+k}}{F_kF_bF_j}
 =\chi_N(j,b,k)\frac{s_{b+k}s_{j+k}}{s_ks_bs_j},
 \tag{2}
\]
\[
 \chi_N(j,b,k)=
 \kappa x^{-b-j}Q^{jb}(-i)^k
                    q^{\,k(b+j)+k(k+1)/2},\qquad |\chi_N|=1.
 \tag{3}
\]
Indeed \(F_h=(-i)^h q^{h(h+1)/2}s_h\); substitution proves (3).
All other matrix entries are zero. No physical entry is a sum of
terms whose phases have been replaced by magnitudes.

For real \(\rho=(\rho_a,\rho_b,\rho_c,\rho_e)\), put
\[
 W_{\rm in}|a,b\rangle=e^{\rho_a a+\rho_b b}|a,b\rangle,\quad
 W_{\rm out}|c,e\rangle=e^{\rho_c c+\rho_e e}|c,e\rangle,\quad
 R^\pm_\rho=W_{\rm out}R^\pm W_{\rm in}^{-1}.
 \tag{4}
\]
Write \(z=(u,v,t)=(j,b,k)/N\), and define
\[
 \lambda_+(\rho)=(\rho_e-\rho_a,\rho_c-\rho_b,\rho_c-\rho_a).
 \tag{5}
\]
Thus the added logarithmic weight of (2) is exactly \(N\lambda_+\cdot z\).
These are prescribed positive diagonal changes, not a new source.
In a contraction their inverse interface factors must be retained.

The original negative crossing satisfies the exact balanced identity
\[
 R^-=\mathsf P\,\overline{R^+}\,\mathsf P,\qquad
 R^-_\rho=\mathsf P\,\overline{R^+_{\rho^\leftrightarrow}}\,\mathsf P,
 \quad \rho^\leftrightarrow=(\rho_b,\rho_a,\rho_e,\rho_c).
 \tag{6}
\]
Here \(\mathsf P\) flips the two physical heads; this is not transpose.
It also follows directly by conjugating the finite Euler coefficients
in [B] and moving the Cartan diagonal. The negative variables are
\((u,v,t)=(b-k,a,k)/N\), with output \((b-k,a+k)\), and
\(\lambda_-(\rho)=\lambda_+(\rho^\leftrightarrow)\).

## 2. A fixed open chamber of unique interior maxima

Set
\[
 h(s)=\int_0^s\log(2\sin\pi r)\,dr,\quad
 \mathcal D=\{u,v,t\ge0:\ u+t\le1,\ v+t\le1\},
\]
\[
 S(z)=h(u+t)+h(v+t)-h(u)-h(v)-h(t),\qquad
 S_\lambda=S+\lambda\cdot z .
 \tag{7}
\]
The actual grid has both upper sums at most \(1-1/N\).
The endpoint-uniform estimate in [W], or the proof below, gives
\(\log s_j=Nh(j/N)+O(\log N)\).

At \(\lambda=0\), fixing \(0<t<1\) gives strictly concave functions
of \(u\) and \(v\). Their unique maxima are \(u=v=(1-t)/2\), since
\[
 \partial_u^2 S
 =-\frac{\pi\sin\pi t}{\sin\pi u\sin\pi(u+t)}<0.
\]
The derivative of the reduced maximum is \(\log\cot(\pi t/2)\).
Its endpoint values are zero. Hence the unique global maximum is
\[
 z_0=(1/4,1/4,1/2),\quad
 M_0=2G/\pi,\quad
 H_0=-S''(z_0)
 =\pi\begin{pmatrix}2&0&1\\0&2&1\\1&1&2\end{pmatrix},
 \quad\det H_0=4\pi^3 ,
 \tag{8}
\]
where \(G=\sum_{r\ge0}(-1)^r/(2r+1)^2\); [W] fixes this value.

There is a fixed closed real ball \(\Lambda\) about zero, with nonempty
interior, such that every \(S_\lambda\), \(\lambda\in\Lambda\), has a
unique interior global maximizer \(z_\lambda\). Its Hessian
\(H_\lambda=-S''(z_\lambda)\) is uniformly positive definite.
Here is also a global justification: choose a small convex neighborhood
of \(z_0\) on which \(-S''\) is positive definite. The complete compact
complement has a strict loss at zero tilt. Small linear tilts preserve
that loss, and the implicit-function theorem supplies the unique
critical point inside the neighborhood. Shrink \(\Lambda\) once.
All statements below are uniform on this fixed chamber.

Put \(M_\lambda=S_\lambda(z_\lambda)\), and
\[
 a(z)=\left[
 \frac{\sin\pi(u+t)\sin\pi(v+t)}
      {\sin\pi u\sin\pi v\sin\pi t}\right]^{1/2},
 \qquad a_\lambda=a(z_\lambda)>0 .
 \tag{9}
\]
No geometric point or unknown closed value defines these quantities.
The maximum and derivatives are those of the explicit three-variable
real function (7).

## 3. The all-order whole-matrix statement

There are explicitly specified real polynomials \(P_{\lambda,l}(y)\),
analytic in \(\lambda\), with \(P_{\lambda,0}=1\) and
\(\deg P_{\lambda,l}\le3l\), with the following property.
For any fixed integer \(J\ge0\), define a matrix
\(\mathcal G^+_{N,J,\rho}\) on the exact support (2) by
\[
 (\mathcal G^+_{N,J,\rho})_{(b+k,j);(j+k,b)}
 =\chi_N(j,b,k)\frac{a_\lambda e^{NM_\lambda}}{\sqrt{2N}}\,
 e^{-y^{\mathsf T}H_\lambda y/2}
       \sum_{l=0}^J N^{-l/2}P_{\lambda,l}(y),
 \quad y=\frac{(j,b,k)-Nz_\lambda}{\sqrt N},
 \quad\lambda=\lambda_+(\rho).
 \tag{10}
\]
It is zero at every other entry. Define the negative model by the same
flip-conjugation as (6).

**Theorem.** For either sign, uniformly when its induced tilt belongs
to \(\Lambda\),
\[
 \boxed{\quad
 \frac{\|R^\pm_\rho-\mathcal G^\pm_{N,J,\rho}\|_{\rm HS}}
      {\|R^\pm_\rho\|_{\rm HS}}
       \le C_J N^{-(J+1)/2}.
 \quad}                                                    \tag{11}
\]
In particular a sufficiently small fixed ball of four boundary weights
works simultaneously for both signs, at all sufficiently large integer
levels, without a parity restriction. Moreover
\[
 \|R^\pm_\rho\|_{\rm HS}^2
 =\sqrt N\,\frac{\pi^{3/2}a_\lambda^2}
                    {2\sqrt{\det H_\lambda}}\,
       e^{2NM_\lambda}(1+O(N^{-1})),
 \quad \lambda=\lambda_\pm(\rho).
 \tag{12}
\]
At zero tilt this is \(\sqrt N\,e^{4GN/\pi}/4\,(1+O(N^{-1}))\).

We specify the correction polynomials and prove the global error.
On a fixed compact subinterval of \(0<x<1\), the sine product has,
for every fixed order, an expansion
\[
 s_n=\sqrt{2N\sin\pi x}\,e^{Nh(x)}
           \left(1+\sum_{r=1}^L N^{-r}b_r(x)+O_L(N^{-L-1})\right),
 \quad x=n/N .
 \tag{13}
\]
The coefficient functions are real analytic on interior intervals;
the remainder bound is needed only on the actual grid. To obtain it,
write \(\log(2\sin\pi x)=\log(2\pi x)+g(x)\), where
\(g=\log(\sin\pi x/(\pi x))\) is smooth at zero.
Apply the finite Euler--Maclaurin formula to \(\sum g(j/N)\) and
the factorial form of the same formula to \(\log(n!)\), with its
\(\tfrac12\log(2\pi)\) constant fixed by the Wallis product.
Their leading terms combine to
\(Nh(x)+\tfrac12\log(2N\sin\pi x)\).
At each requested order, apply the formulas two orders farther:
the integral remainder is bounded by the next power of \(N^{-1}\)
times a fixed derivative bound. This proves the asserted grid remainder.
Subtracting also \(\log(1-x)\) leaves a smooth function on the full
interval and proves the weaker endpoint estimate used above.

Consequently the positive amplitude in (2), including its tilt, is
\[
 \frac{a(z)}{\sqrt{2N}}e^{NS_\lambda(z)}
       \left(1+\sum_{r=1}^L N^{-r}c_r(z)+O_L(N^{-L-1})\right)
 \tag{14}
\]
uniformly on an interior neighborhood of all \(z_\lambda\).
The \(c_r\) are fixed by the five products in (2), not fitted data.
With a formal variable \(\eta\), define \(P_{\lambda,l}\) as the
coefficient of \(\eta^l\) in
\[
 \frac{a(z_\lambda+\eta y)}{a_\lambda}
 \left(1+\sum_{r\ge1}\eta^{2r}c_r(z_\lambda+\eta y)\right)
 \exp\left\{\sum_{r\ge3}\frac{\eta^{r-2}}{r!}
                           S^{(r)}(z_\lambda)[y^r]\right\}.
 \tag{15}
\]
Only finitely many derivatives enter each coefficient.
Every monomial has degree at most three times its \(\eta\)-order,
and \(P_{\lambda,l}(-y)=(-1)^lP_{\lambda,l}(y)\).

For completeness, fix \(J\) and choose a small \(\beta>0\), for example
\(\beta<1/(12(J+2))\). On \(|y|\le N^\beta\), Taylor's formula in
(14)--(15), with \(L\) sufficiently large, bounds the entry error by
\[
 C_J\,\frac{e^{NM_\lambda}}{\sqrt N}\,
 N^{-(J+1)/2}(1+|y|^{C_J})e^{-c|y|^2}.
 \tag{16}
\]
The bound follows by keeping the exponential remainder:
\(N|z-z_\lambda|^3\le C N^{-1/2}|y|^3=o(1)\) there.
The omitted Taylor terms have the stated power of \(N^{-1/2}\)
times a fixed polynomial. Positive definiteness absorbs their
remaining exponential factors into the displayed Gaussian.
The lattice spacing in \(y\) is \(N^{-1/2}\), so the sum of a fixed
Gaussian polynomial is \(O(N^{3/2})\), uniformly in the shifted center.
The squared error from (16) is therefore at most
\(C_J\sqrt N e^{2NM_\lambda}N^{-J-1}\).

On the rest of a fixed interior neighborhood, strict concavity gives
the same Gaussian upper bound for (14), and for (10).
The part \(|y|>N^\beta\) is smaller than every power of \(N^{-1}\).
Outside that neighborhood the compact global loss and the
endpoint-uniform \(O(\log N)\) estimate give at most a polynomial
times \(e^{2N(M_\lambda-\gamma)}\) for the squared norm.
The model has the same negligible tail by its Gaussian bound.
A ball of \(O(\sqrt N)\) lattice indices about \(Nz_\lambda\) gives
the uniform lower bound \(c\sqrt N e^{2NM_\lambda}\) for
\(\|R^+_\rho\|_{\rm HS}^2\). These estimates prove (11) globally.

To obtain (12), use \(J=1\). The term of order \(N^{-1/2}\) in the
squared model is odd in \(y\), by (15). Gaussian-polynomial lattice
sums differ from their continuum integrals by \(O(e^{-cN})\), uniformly
in their shift: periodize the Gaussian on the mesh, compute its Fourier
coefficients by the real Gaussian integral, and differentiate that
formula for polynomial factors. Every nonzero dual lattice point has
an \(e^{-cN|m|^2}\) factor. Extending our interior lattice to all of
\(\mathbb Z^3\) costs only an exponential tail.
The leading integral is \(\pi^{3/2}/\sqrt{\det H_\lambda}\).
Together with \(N^3/(2N)\) and the Gaussian scale \(N^{-3/2}\)
this gives (12). Equation (6) proves all negative-sign assertions.

## 4. Full packets, interfaces, and scope

At zero tilt, [P] identifies the complete physical algebra
\(\mathcal A_N=\mathbb C[\Omega]\) as an \(N\)-dimensional subspace
of these pair matrices. Let \(\Pi_N\) be its physical orthogonal
projection. Since \(R^\pm\in\mathcal A_N\), projection cannot increase
the error in (11). Thus \(\Pi_N\mathcal G^\pm_{N,J,0}\) is an actual
full-boundary approximation at the same rate. No value quotient or
deletion of double-root normal directions occurs.

For nonzero tilts the correct space is the exact linear image
\(W_{\rm out}\mathcal A_NW_{\rm in}^{-1}\); its orthogonal projection
has the same contraction property in the Hilbert--Schmidt norm of
the gauged arrays.
It need not be the original algebra or preserve multiplication.
Undoing the gauges can cost exponentially in \(N\). Both incident
interface factors, original caps and physical budgets must therefore
be retained in a proposed network use. No free transfer of (11) to
an untilted whole-component error or unchanged new budgets is claimed.
The two Gaussian models are not asserted to be exact mutual inverses.

[W] already proves the compact weighted norm rate and the unique flat
maximum. [G, Section 4] already proves a full Hilbert--Schmidt Gaussian
operator limit for the \(N\times N\) Newton-coordinate crossing.
That coefficient-space metric differs from the uniform physical
\(N^2\times N^2\) array here. The Newton row covariance in [N] and
the coherent lower-donor kernels in [H] are further closest coverage.
The present addition is the entire physical-matrix Gaussian expansion
with arbitrary fixed-order Hilbert--Schmidt errors and its prefactor.
No general novelty for lattice Laplace expansions is claimed.
Small boundary tilts have not been matched to arbitrary geometric
Conway data. Even a full-matrix relative error can exceed the original
closing overlap. Neither a whole short-component propagation theorem
nor a scalar geometric lower or finite-exception theorem follows.

## Complete inputs and coverage

All six complete matching texts were read. Only written mathematics
and text/hash operations were used; no earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| B, input, 247 lines | [Balanced physical crossing](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/balanced_verma_coherent_braiding.md) | 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4 |
| W, input, 244 lines | [Weighted crossing rate](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/weighted_crossing_source_gap.md) | a6a6411a780c904493db4fca3b5536f902aa5be8b6ef7cfb880a4f57509f436c |
| P, input, 477 lines | [Uniform physical algebra](research_conway_uniform_physical_quartic.md) | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| N, coverage, 415 lines | [Newton row covariance](research_actual_newton_crossing_gaussian_covariance.md) | ce2b1b8efbbcffa8bafe0d0de4f7ce12febf193e433d8e3291f7d2a8c826fa3f |
| H, coverage, 398 lines | [Physical hybrid lower kernel](research_physical_crossing_hybrid_lower_kernel.md) | 3025b561b9e30503de6eb2fe6ca265f04cfa730313c77c2156d3fc3b35f8926f |
| G, coverage, 468 lines | [Newton full Gaussian operator limit](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_one_crossing_gaussian_window.md) | d5d8611da7158539ee73af5413ab2f59da50afe5d3d43dcf2631f4c28f373683 |
