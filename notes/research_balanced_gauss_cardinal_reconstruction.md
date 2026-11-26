# An actual scalar unit after balanced Gauss reconstruction

Private written proof, 18 November 2026.

The full finite Fourier reconstruction in C has a nonzero analytic
asymptotic on a fixed complex neighborhood of a lower-triangle point.
The coefficient of that branch is one: it is the double cardinal
residue, and the entire complementary array and all boundary integrals
have an exponential gap. Both finite Fermat numerators remain in the
argument. The proof also covers a scaled meridian disk and its actual
fixed-quantum meridian derivatives.

The positive triangle entropy and its Gaussian windows are existing
results in O. The new assertion is for the reconstructed scalar
polynomial, including between-grid complex arguments, not just that
positive weight or a dechirped window. No actual matrix/coherent
substitution or closed-source noncancellation is inferred.

## 1. Statement for the actual finite polynomial

Put \(c_0=2\pi i\), \(Q=e^{c_0/N}\), \(d=N-1\), and
\[
 M=e^{\xi/N},\qquad \beta=-2\xi/c_0,\qquad
 c=M^{-2}Q=e^{c_0(1+\beta)/N}.
 \tag{1}
\]
Fix \(0<\eta<\pi\). C's exact scalar polynomial is
\[
 \mathcal S_N(u,v;c)=\sum_{l,k=0}^d C_{lk}(c)L_l(u)L_k(v),
 \quad C_{lk}=\frac{(c;Q)_{l+k}}{(c;Q)_l(c;Q)_k},\quad
 L_l(u)=\frac1N\sum_{j=0}^d(uQ^{-l})^j.
 \tag{2}
\]
It is exactly the balanced finite Gauss polynomial with
\(a=u^{-1},b=v^{-1},t=c/(ab)\). In particular the balance
\(abt=c\), and its root value \(abt=Q\), are unchanged.

Let \(\mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt\) on the
real unit interval, and continue its differences holomorphically near
the strict triangle. Define
\[
 \begin{split}
 H(x,y)&=\mathcal J(x+y)-\mathcal J(x)-\mathcal J(y),\\
 \Phi(x,y)&=H(x,y)+i\pi xy,\\
 \Lambda(x,y)&=\frac{\pi\sin\pi(x+y)}{\sin\pi x\sin\pi y}.
 \end{split}\tag{3}
\]
All branches below are continued from the real strict triangle;
\(\Lambda\) is positive there and its logarithm is real.

**Theorem.** There is a fixed complex bidisk \(\mathcal U\)
about \((1/3,1/3)\) such that, uniformly on a slightly smaller
closed bidisk and \(|\xi|\le\eta\),
\[
 \boxed{\quad
 \mathcal S_N(e^{c_0x},e^{c_0y};e^{c_0(1+\beta)/N})
 =\frac{\Gamma(1+\beta)N^{-\beta}\Lambda(x,y)^\beta}
          {\sqrt{2N}}
  \sqrt{\frac{\sin\pi(x+y)}{\sin\pi x\sin\pi y}}
  e^{N\Phi(x,y)}\bigl(1+O(N^{-1})\bigr).
 \quad}\tag{4}
\]
The square root is positive on the real triangle. All fixed derivatives
of the normalized relative error are \(O(N^{-1})\) after shrinking
the domains. In particular the exact polynomial is nonzero there for
all sufficiently large \(N\).

More precisely, the proof constructs a holomorphic nonzero surrogate
\(\mathcal B_N(x,y,\beta)\) on the specified bulk domain such that
\[
 \mathcal S_N(e^{c_0x},e^{c_0y};c)
       =\mathcal B_N(x,y,\beta)\bigl(1+O(e^{-\varepsilon N})\bigr),
 \tag{5}
\]
uniformly with fixed derivatives on smaller domains. The surrogate
is not declared to interpolate the exact samples: its exponentially
small sample error is included in (5).

## 2. An exponentially accurate holomorphic factorial surrogate

Choose a real bulk interval containing the eventual \(x,y,x+y\)
values and lying strictly inside \((0,1)\). On a complex tube about
the interval from zero to its upper endpoint, the function
\[
 f(z)=\Log\frac{1-e^{c_0z}}{-c_0z},\qquad f(0)=0,
 \tag{6}
\]
is holomorphic. The tube is chosen away from the nonzero integer
zeros. The logarithm is continued from zero. On a slightly smaller
tube there are constants \(C,R>0\) with
\(|f^{(k)}|\le Ck!R^{-k}\).

Take \(\eta<\eta_1<\pi\), so \(|\beta|\le\eta_1/\pi<1\),
and choose a sufficiently small fixed \(\alpha>0\).
For \(L=\lfloor\alpha N\rfloor\), define
\[
 \begin{split}
 \mathcal E_N(x,\beta)={}&
 N\int_{\beta/N}^{x+\beta/N}f(z)\,dz
 +\tfrac12\{f(x+\beta/N)-f(\beta/N)\}\\
 &+\sum_{k=1}^{L}\frac{B_{2k}}{(2k)!}N^{1-2k}
       \{f^{(2k-1)}(x+\beta/N)-f^{(2k-1)}(\beta/N)\}.
 \end{split}\tag{7}
\]
Integrals use the fixed holomorphic primitive in this tube. Set
\[
 G_N(x,\beta)=
    (-c_0/N)^{Nx}
    \frac{\Gamma(Nx+1+\beta)}{\Gamma(1+\beta)}
       \exp\mathcal E_N(x,\beta),
 \quad \Log(-c_0)=\log(2\pi)-i\pi/2.
 \tag{8}
\]
This is holomorphic and nonzero on the specified bulk domain for
large \(N\). Its Gamma arguments there stay away from the poles;
no global holomorphy assertion for (8) is needed.

For an integer \(n=Nx\) in the protected real bulk, the exact product is
\[
 (c;Q)_n=(-c_0/N)^n
       \frac{\Gamma(n+1+\beta)}{\Gamma(1+\beta)}
       \exp\sum_{j=1}^n f((j+\beta)/N).
 \tag{9}
\]
Euler--Maclaurin on the shifted segment gives the sum in (9) as
(7) plus a remainder. The periodic Bernoulli bound
\(\|B_{2L}(\{t\})\|/(2L)!\le4/(2\pi)^{2L}\), together with
the displayed Cauchy derivative bound, bounds its absolute value by
\[
 C N\frac{(2L)!}{(2\pi RN)^{2L}}
       \le C N\left(\frac{L}{\pi RN}\right)^{2L}
       \le e^{-\gamma N}
 \tag{10}
\]
for some \(\gamma>0\), after decreasing \(\alpha\).
The harmless adjustment of \(R\) absorbs the \(O(N^{-1})\)
complex shifts. The remainder formula is valid for complex \(\beta\)
by parameterizing the segment by its real coordinate, and all bounds
are uniform on the larger \(\beta\)-disk. Therefore
\[
             (c;Q)_n=G_N(n/N,\beta)(1+O(e^{-\gamma N})).
 \tag{11}
\]
Cauchy on the larger parameter disk proves the same exponential
accuracy for every fixed \(\beta\)-derivative of the relative sample
error. No finite collection of small coefficient errors has been
summed without this long remainder estimate.

## 3. The calibrated bulk phase and amplitude

The terms in (7) beyond the endpoint term are \(O(N^{-1})\)
uniformly on a smaller complex bulk tube: the Cauchy and Bernoulli
bounds make their successive bounds decrease when \(k\le\alpha N\).
Taylor expansion of the two shifted endpoints consequently gives
\[
 \mathcal E_N(x,\beta)-\mathcal E_N(x,0)
                      =\beta f(x)+O(N^{-1}).
\]
The fixed-sector Gamma ratio gives
\[
 \frac{G_N(x,\beta)}{G_N(x,0)}
 =\frac{N^\beta B(x)^\beta}{\Gamma(1+\beta)}
                       (1+O(N^{-1})),\qquad
 B(x)=\frac{1-e^{c_0x}}{-c_0}.
 \tag{12}
\]
The logarithm of \(B\) is \(\Log x+f(x)\), continued from
positive small \(x\). All these errors and fixed derivatives are
uniform on smaller domains.

For completeness the root phase is fixed directly by (9), rather than
by an unspecified off-grid \((-1)^n\). Stirling in (8), at \(\beta=0\),
gives
\[
 G_N(x,0)=\sqrt{2\pi N B(x)}\,e^{NI(x)}(1+O(N^{-1})),
 \quad I(x)=\int_0^x\Log(1-e^{c_0t})\,dt.
 \tag{13}
\]
Here the integrable endpoint logarithm uses the branch specified in
(8). On \(0<x<1\),
\[
 I(x)=\mathcal J(x)+\tfrac{i\pi}{2}(x^2-x),\qquad
 B(x)=e^{i\pi x}\sin(\pi x)/\pi.
 \tag{14}
\]
Thus the exact grid phase is the original
\(f_n=(-i)^nq^{n(n+1)/2}s_n\), not a different interpolation
of its sign.

Define on the protected two-variable bulk
\[
          \mathcal B_N(x,y,\beta)
              =\frac{G_N(x+y,\beta)}{G_N(x,\beta)G_N(y,\beta)}.
 \tag{15}
\]
At every lower-triangle grid point in that bulk, (11) gives
\[
 C_{lk}(c)=\mathcal B_N(l/N,k/N,\beta)
                         (1+O(e^{-\gamma N})).
 \tag{16}
\]
Equations (12)--(14) give exactly the right side of (4) for
\(\mathcal B_N\). Indeed \(I(x+y)-I(x)-I(y)=\Phi(x,y)\),
and \(B(x+y)/(B(x)B(y))=\Lambda(x,y)\) is positive on the
real triangle. In particular \(\mathcal B_N\) is bounded above
and below by a polynomial in \(N\) times \(e^{N\Re\Phi}\),
uniformly on the parameter domains.

## 4. The exact cardinal residue, with both Fermat factors

For an external coordinate \(x\), define
\[
 \mathcal K_N(x,z)=
 \frac{c_0(e^{c_0Nx}-1)}
      {(e^{c_0Nz}-1)(e^{c_0(x-z)}-1)}.
 \tag{17}
\]
At a grid point \(z=l/N\), its residue is
\(L_l(e^{c_0x})\). At \(z=x\), its residue is \(-1\).
Take a rectangle \(\mathcal R_N\) of width less than one, with
vertical sides at half-grid real parts and horizontal sides at fixed
heights \(\pm h\). If \(x\) lies in its interior, a holomorphic
function \(F\) on the rectangle satisfies exactly
\[
 \sum_{l/N\in\mathcal R_N}L_l(e^{c_0x})F(l/N)
  =F(x)+\frac1{2\pi i}\int_{\partial\mathcal R_N}
                                      \mathcal K_N(x,z)F(z)\,dz.
 \tag{18}
\]
Only grid points on the real axis enter the sum. The identity extends
to external grid points by holomorphic continuation. No root of
\(e^{c_0Nx}-1\) is removed before this identity is used.

Use the same construction in both variables. For an analytic
\(F(z,w)\), the boxed interpolation is exactly
\[
 F(x,y)+\mathcal R_xF(\cdot,y)
             +\mathcal R_yF(x,\cdot)+\mathcal R_x\mathcal R_yF,
 \tag{19}
\]
where each \(\mathcal R\) denotes the boundary integral in (18).
The two single-boundary terms and the double-boundary term are all
retained. The coefficient of the evaluation is \(+1\).

If the external target remains a fixed positive distance from the
rectangle boundary, then on that boundary
\[
 |\mathcal K_N(x,z)|\le C
  \exp\{2\pi N(-\Im x)_+-2\pi N(-\Im z)_+\}.
 \tag{20}
\]
On a vertical half-grid side,
\(|e^{c_0Nz}-1|=1+e^{-2\pi N\Im z}\) exactly. On the
two horizontal sides its corresponding bound follows from the fixed
height. The remaining denominator is bounded away from zero on the
boundary. This proves (20) with the full numerator cost retained.

## 5. A gap for every boundary term

O proves the endpoint-uniform bound
\(\log|C_{lk}(Q)|=NH(l/N,k/N)+O(\log N)\) on the lower
triangle, and that \(H\) has the unique global maximum
\[
 H_* =H(1/3,1/3)>0.
 \tag{21}
\]
Its strict concavity also follows from
\[
 -H''=\pi\begin{pmatrix}
 \cot\pi x-\cot\pi(x+y)&-\cot\pi(x+y)\\
 -\cot\pi(x+y)&\cot\pi y-\cot\pi(x+y)
 \end{pmatrix},\qquad \det(-H'')=\pi^2.
\]
Both diagonal entries are positive in the strict triangle. These
known entropy facts are used only to control complements of the
actual reconstruction.

Choose a fixed small real box about \((1/3,1/3)\), whose doubled
box lies strictly in the triangle. Place the vertical sides of
\(\mathcal R_N\) at the nearest half-grid positions to its endpoints.
For all large \(N\), the real complement of the grid box has a fixed
entropy loss \(g>0\). Its vertical edges have the same loss, uniformly
when the other real coordinate is in the box.

There is also a strict horizontal loss after including (20). For
real \(t,s\) in the doubled box and small real \(\sigma,\tau\),
\[
 \Re\Phi(t+i\sigma,s+i\tau)
   =H(t,s)-\pi(s\sigma+t\tau)+O(\sigma^2+\tau^2).
\]
Since both real coordinates lie in a fixed compact subset of
\((0,1)\), some \(\omega>0\) satisfies
\[
 \Re\Phi(t+i\sigma,s+i\tau)
   -2\pi\{(-\sigma)_++(-\tau)_+\}
 \le H(t,s)-\omega(|\sigma|+|\tau|)
                          +C(\sigma^2+\tau^2).
 \tag{22}
\]
Choose \(h>0\) small enough that the quadratic term is at most
half of the linear loss on \(|\sigma|,|\tau|\le h\).
On a horizontal face one height equals \(h\) in modulus; on a
vertical face the real entropy already has its gap. Consequently
there is \(g_1>0\) such that the effective phase on every boundary
piece in (19) is at most \(H_*-g_1\), apart from the external
target costs in (20).

For the single-boundary terms the unintegrated external imaginary
coordinate can add at most \(C\delta_0\) if the target bidisk has
radius \(\delta_0\). The two Fermat numerator costs in all terms
are at most \(4\pi\delta_0\). Shrink \(\delta_0\) so that these
costs are smaller than \(g_1/4\). The amplitude bounds following
(16), and the finite lengths of the boundaries, then show that each
of the three boundary terms for \(F=\mathcal B_N\) is bounded by
\[
                 C N^p e^{N(H_*-g_2)}
 \tag{23}
\]
for a fixed \(g_2>0\), uniformly on the scaled meridian disk.
This includes the corners; none is replaced by an independent
stationary phase assertion.

## 6. The whole complementary array and the sample error

C's exact frame factorization gives, for the lower triangle,
\[
 |C_{lk}(c)|\le C N^p |C_{lk}(Q)|
                      \qquad (|\xi|\le\eta_1).
 \tag{24}
\]
For the entire upper triangle C proves a polynomial bound on that
same scaled collar. Thus the lower points outside the box contribute
at most a polynomial times \(e^{N(H_*-g)}\), and the whole upper
triangle contributes only a polynomial, before the scalar cardinal
factors are evaluated.

The exact elementary bound
\[
 |L_l(e^{c_0x})|\le\max(1,|e^{c_0x}|)^d
                            \le e^{2\pi N(-\Im x)_+}
 \tag{25}
\]
retains both external boundary characters. Taking a smaller fixed
target bidisk if necessary, (21),(24),(25) give a positive gap for
the entire array outside the box, including the upper triangle.
The number of entries is only \(N^2\).

Inside the box replace the exact samples by (16). Their total error
is bounded by a polynomial times
\(e^{N(H_*-\gamma+4\pi\delta_0)}\), using (25).
Choose \(\delta_0\) smaller once more to retain this gap as well.
Equation (19) and the boundary estimate (23) now prove
\[
 |\mathcal S_N-\mathcal B_N|
                  \le C N^p e^{N(H_*-g_3)}
 \tag{26}
\]
for some \(g_3>0\). Finally shrink the target so that
\(\Re\Phi(x,y)>H_*-g_3/4\). The lower polynomial-amplitude
bound for the nonzero \(\mathcal B_N\) converts (26) into (5),
after absorbing polynomial factors into a smaller exponential gap.
Equations (12)--(16) then give (4).

All estimates were established on larger fixed complex domains in
\(x,y,\xi\). Cauchy applied to the holomorphic relative errors,
on smaller domains, proves the asserted derivative statements.
No derivative of an uncontrolled pointwise asymptotic is taken.
Both level parities and every retained finite cap are included.

## 7. Actual meridian derivatives and source scope

At fixed scalar \(x,y\), the theorem is an asymptotic for the
literal finite polynomial in \(c=M^{-2}Q\). Its first meridian
normal is therefore determined, rather than inferred from a
meridian-independent root phase. From (4), at \(M=1\),
\[
 \left.\partial_\mu\Log
   \mathcal S_N(e^{c_0x},e^{c_0y};Qe^{-2\mu})\right|_0
   =\frac{2N}{c_0}
        \{\log N+\gamma_{\rm E}-\Log\Lambda(x,y)\}+O(1).
 \tag{27}
\]
Here \(\gamma_{\rm E}\) is Euler's constant, and the branch of
\(\Log\Lambda\) is the one in (3). This follows from
\(\partial_\mu=N\partial_\xi\),
\(\partial_\xi\beta=-2/c_0\), and \(\psi(1)=-\gamma_{\rm E}\),
with the differentiated relative remainder justified above.
All fixed scaled-meridian jets are similarly controlled by (4),(5).

The original actual factor is still
\(\mathcal A_N=H_dK^d\mathcal S_N(u,v;c)\), with
\(u+v=\Omega/(qK)\), \(uv=(QK^2)^{-1}\), and with C's
specified symmetric polynomial evaluation. Its exterior braid,
turnover, source normalization, pivot, and marks are unchanged.
If scalar arguments move within the proved domain, their derivatives
use the ordinary chain rule in addition to (27). Arbitrary evaluated
matrix/Jordan norms or coherent kernels do not follow from a scalar
estimate, and their moving operator coupons are not reset.

The domain contains regular nonreal scalar points after moving off
the diagonal \(x=y\); no assertion places every complete geometric
representation there. The theorem proves an actual reconstructed
scalar branch with coefficient one. It does not identify a physical
geometric cycle, remove the other exterior factors, or prove a
nonzero closed knot asymptotic. Quantum-parameter normals remain
outside this fixed-root theorem.

## Complete proof directs

* C: notes/research_balanced_gauss_cyclic_divisor_source.md,
  SHA256 c15668d7dff95346d72801b721bf95970b661e5b17d125aaadd7e0dc38905b00.
* O: notes/research_one_crossing_gaussian_window.md,
  SHA256 d5d8611da7158539ee73af5413ab2f59da50afe5d3d43dcf2631f4c28f373683.

Both complete directs and the entire final were read nontruncated in
the author sequence; every used implication and pin was checked.
Only written mathematics and text/hash operations were used. Frozen
and public files were not edited.
