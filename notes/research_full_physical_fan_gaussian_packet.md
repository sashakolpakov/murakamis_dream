# A joint physical Gaussian packet for a fixed crossing fan

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

A fixed positive fan has one transfer path at each nonzero matrix entry.
Its whole physical Hilbert--Schmidt norm and joint Gaussian packet can
therefore be calculated before any closing. The result includes a
nonzero coefficient between independently specified product Gaussian
boundary vectors. It does not estimate the prescribed knot closing.
The same bipyramid volume already occurs in the Fourier bridge
coordinates of [B]; the new assertions concern the original physical
fan matrix, its joint norm, and its prepared physical boundary vectors.

## 1. The exact fan, including its phase

Fix an integer \(r\ge1\), independently of \(N\ge2\). Put

\[
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x_0=-q^{-1},
 \quad \kappa=q^{D^2/2},\quad
 s_j=\prod_{h=1}^j2\sin(\pi h/N),\quad s_0=1.
\]

Use the uniform physical orthonormal head basis of [G]. All matrix
norms below are unnormalized Hilbert--Schmidt norms unless specified.
Let \(R_i^+\) act on heads \(i,i+1\), and set

\[
 \mathsf F_{r,N}=R_r^+\cdots R_1^+.
 \tag{1}
\]

For input \((a,b_1,\ldots,b_r)\), write \(K_i=k_1+\cdots+k_i\),

\[
 d=a-K_r,\qquad j_i=a-K_i=d+\sum_{h>i}k_h.
\]

The output is \((b_1+k_1,\ldots,b_r+k_r,d)\). Its nonzero support is
exactly

\[
 d,k_i,b_i\ge0,\qquad d+\sum_i k_i\le D,\qquad b_i+k_i\le D.
 \tag{2}
\]

The input and output determine every \(k_i\), so there is no internal
sum at one entry. The exact coefficient in [G, (2)--(3)] telescopes to

\[
 (\mathsf F_{r,N})_{\rm out,in}
 =\Xi_N(d,\boldsymbol k,\boldsymbol b)
       \frac{s_a}{s_d}\prod_{i=1}^r
                      \frac{s_{b_i+k_i}}{s_{b_i}s_{k_i}},
 \quad \Xi_N=\prod_{i=1}^r\chi_N(j_i,b_i,k_i),
 \tag{3}
\]

\[
 \chi_N(j,b,k)=\kappa x_0^{-j-b}Q^{jb}(-i)^k
                       q^{k(j+b)+k(k+1)/2},\qquad |\Xi_N|=1.
\]

All powers mean the displayed exponentials. The Cartan scalar is
\(\kappa^r\); it has not been removed. The integer coordinates
\(n=(d,\boldsymbol k,\boldsymbol b)\) in (2) parametrize entries
once, on a primitive lattice of dimension \(\ell=2r+1\).

## 2. The complete joint maximum

Write \(z=(x,\boldsymbol t,\boldsymbol v)=n/N\), \(T=\sum_i t_i\),
and \(\mathfrak a=x+T\). Define

\[
 h(u)=\int_0^u\log(2\sin\pi v)\,dv,\qquad
 S_r(z)=h(\mathfrak a)-h(x)+
               \sum_i\{h(v_i+t_i)-h(v_i)-h(t_i)\}.
 \tag{4}
\]

Its compact domain is \(x,t_i,v_i\ge0\), \(x+T\le1\),
\(v_i+t_i\le1\). The uniform factorial bound of [G] gives the
entry rate \(NS_r+O_r(\log N)\) on the entire finite support.

For fixed \(0<t<1\), \(h(v+t)-h(v)-h(t)\) is strictly concave
in \(v\in(0,1-t)\), since its second derivative is
\(-\pi\sin(\pi t)/(\sin\pi v\sin\pi(v+t))<0\).
Its maximum is at \(v=(1-t)/2\), and its value is
\(-2h(t/2)\). Here reflection \(h(1-u)=-h(u)\) and

\[
 h(2u)=2h(u)-2h(1/2-u),\qquad 0\le u\le1/2,
\]

prove the value; the latter identity follows by differentiation and
its zero value at \(u=0\). Continuity includes \(t=0,1\).
For fixed \(\mathfrak a=a\) and \(T=K\), strict convexity of \(h\)
on \([0,1/2]\) gives equal \(t_i=K/r\). Thus the remaining maximum is

\[
 \max_{0\le K\le a}
     \{h(a)-h(a-K)-2r h(K/(2r))\}
 =I_r(a):=h(a)-(2r+1)h(a/(2r+1)).
 \tag{5}
\]

Indeed the derivative in \(K\) is
\(\log[\sin\pi(a-K)/\sin(\pi K/(2r))]\).
For \(0<K<a\le1\), the sum of the two sine arguments, divided by
\(\pi\), is less than one. The sine-difference formula therefore
makes its sign that of \(a-K-K/(2r)\). This proves the unique
maximum \(K=2ra/(2r+1)\), with endpoint values obtained by continuity.
Finally
\(I_r'(a)=\log[\sin\pi a/\sin(\pi a/(2r+1))]\)
changes sign only at the following point. Put

\[
 \delta=\frac{\pi}{2r+2},\quad
 x_*={1\over2r+2},\quad t_{i,*}={1\over r+1},\quad
 v_{i,*}={r\over2r+2},\quad
 \mathfrak a_*={2r+1\over2r+2}.
 \tag{6}
\]

This is the unique global maximum of \(S_r\), including its boundary,
and

\[
 M_r=-(2r+2)h(1/(2r+2)).
 \tag{7}
\]

Every maximizing transfer is strictly positive, so the possible
nonuniqueness in the recipient optimization at \(t=0\) is irrelevant.

For clarity, (7) is the previously occurring bipyramid value, not a
new volume formula. With \(\Lambda(\theta)=-\int_0^\theta
\log(2\sin u)\,du\), it is
\(2\pi M_r=2(2r+2)\Lambda(\pi/(2r+2))\).
Place \(n_0=2r+2\) equally spaced equatorial vertices on a circle of
the ideal boundary sphere, with the two ideal apices at the poles.
In the Klein ball, subdivision about their axis gives
\(n_0\) ideal tetrahedra with angle triples
\((2\pi/n_0,\pi/2-\pi/n_0,\pi/2-\pi/n_0)\).
The ideal-tetrahedron Lobachevsky formula and its duplication identity
give volume \(2\Lambda(\pi/n_0)\) for each. Thus \(2\pi M_r\) is
the volume of the regular ideal \(n_0\)-gonal bipyramid.

## 3. Hessian, density, and the whole norm

Set \(\alpha=\pi\cot\delta\), \(\beta=\pi\tan\delta\).
In coordinate order \((x,\boldsymbol t,\boldsymbol v)\),
\(H=-S_r''(z_*)\) has blocks

\[
 H_{xx}=2\alpha,\quad H_{x\boldsymbol t}=\alpha\boldsymbol1^{\mathsf T},
 \quad H_{x\boldsymbol v}=0,\quad
 H_{\boldsymbol t\boldsymbol t}
  =\alpha\boldsymbol1\boldsymbol1^{\mathsf T}
                       +{\alpha+\beta\over2}I,
 \quad H_{\boldsymbol t\boldsymbol v}=\beta I,
 \quad H_{\boldsymbol v\boldsymbol v}=2\beta I.
 \tag{8}
\]

Eliminate the \(v\) block and then the \(x\) block. The remaining
Schur block is \((\alpha/2)(I+\boldsymbol1\boldsymbol1^{\mathsf T})\).
Consequently \(H>0\), and

\[
 \det H=2(r+1)\pi^{2r+1}\cot\delta.
 \tag{9}
\]

The interior sine-factorial expansion in [G] gives the entry modulus
\((2N)^{-r/2}A(z)e^{NS_r(z)}(1+O_r(N^{-1}))\), where

\[
 A(z)^2={\sin\pi\mathfrak a\over\sin\pi x}
       \prod_i{\sin\pi(v_i+t_i)\over\sin\pi v_i\sin\pi t_i},
 \qquad A_*^2=\sin(2\delta)^{-r}.
 \tag{10}
\]

**Norm theorem.** Through all sufficiently large integer levels,

\[
 \boxed{\quad
 \|\mathsf F_{r,N}\|_{\rm HS}^2
 =C_r\sqrt N\,e^{2NM_r}(1+O_r(N^{-1})),\qquad
 C_r={ (2\sin(2\delta))^{-r}\over
                         \sqrt{2(r+1)\cot\delta}}.
 \quad}
 \tag{11}
\]

The lattice density is \(N^\ell\), the squared density in (10)
contributes \((2N)^{-r}\), and the Gaussian integral contributes
\(N^{-\ell/2}\pi^{\ell/2}/\sqrt{\det H}\).
Their product is \(\sqrt N\,2^{-r}\pi^{\ell/2}A_*^2/\sqrt{\det H}\),
which is (11). The next section proves the uniform error and both
parities. At \(r=1\), (11) is precisely [G]'s prefactor \(1/4\).

## 4. Full fixed-order packets and real boundary tilts

For prescribed real input weights \((\rho_0,\ldots,\rho_r)\) and
output weights \((\sigma_1,\ldots,\sigma_r,\sigma_0)\), use diagonal
factors \(e^{\rho_0a+\sum\rho_i b_i}\) and
\(e^{\sum\sigma_i(b_i+k_i)+\sigma_0d}\), called
\(W_{\rm in}\) and \(W_{\rm out}\). The gauged fan
\(W_{\rm out}\mathsf F_{r,N}W_{\rm in}^{-1}\) adds exactly

\[
 \lambda_x=\sigma_0-\rho_0,\qquad
 \lambda_{t_i}=\sigma_i-\rho_0,\qquad
 \lambda_{v_i}=\sigma_i-\rho_i
 \tag{12}
\]

to the entropy as \(\lambda\cdot z\). This map is onto; a common
shift of all boundary weights has no effect. Compactness and (8)
give a fixed small closed tilt ball on which the global maximizer
\(z_\lambda\) remains unique and interior, with uniformly positive
\(H_\lambda=-S_r''(z_\lambda)\). Put
\(M_\lambda=S_r(z_\lambda)+\lambda\cdot z_\lambda\),
\(A_\lambda=A(z_\lambda)\).

For every fixed \(J\ge0\), there are real polynomials
\(P_{\lambda,l}(y)\), analytic in \(\lambda\), with
\(P_{\lambda,0}=1\), degree at most \(3l\), and parity \(l\).
On the exact support (2), define the model by

\[
 \mathcal G_{r,N,J,\lambda}
 =\Xi_N(n)(2N)^{-r/2}A_\lambda e^{NM_\lambda}
 e^{-y^{\mathsf T}H_\lambda y/2}
       \sum_{l=0}^J N^{-l/2}P_{\lambda,l}(y),
 \qquad y={n-Nz_\lambda\over\sqrt N}.
 \tag{13}
\]

It is zero elsewhere. If \(\mathsf F_{r,N,\lambda}\) denotes the
gauged array, then uniformly on that ball,

\[
 {\|\mathsf F_{r,N,\lambda}-\mathcal G_{r,N,J,\lambda}\|_{\rm HS}
       \over\|\mathsf F_{r,N,\lambda}\|_{\rm HS}}
 \le C_{r,J}N^{-(J+1)/2},\qquad
 \|\mathsf F_{r,N,\lambda}\|_{\rm HS}^2
 ={2^{-r}\pi^{\ell/2}A_\lambda^2\over\sqrt{\det H_\lambda}}
       \sqrt N e^{2NM_\lambda}(1+O_r(N^{-1})).
 \tag{14}
\]

Here is the quantitative argument, rather than a formal expansion.
The all-order sine-product formula [G, (13)] applied to (3) gives
the density (10) times \(1+\sum_{j\ge1}N^{-j}c_j(z)\), with
analytic \(c_j\) and a uniform remainder at each fixed order.
Define \(P_{\lambda,l}\) by extracting \(\eta^l\) from

\[
 {A(z_\lambda+\eta y)\over A_\lambda}
 \left(1+\sum_{j\ge1}\eta^{2j}c_j(z_\lambda+\eta y)\right)
 \exp\left\{\sum_{j\ge3}{\eta^{j-2}\over j!}
                        S_r^{(j)}(z_\lambda)[y^j]\right\}.
 \tag{15}
\]

Only finitely many derivatives enter. For a small fixed
\(b<1/(12(J+2))\), Taylor remainders on \(|y|\le N^b\) bound
the entry error by
\(C e^{NM_\lambda}N^{-r/2-(J+1)/2}(1+|y|^C)e^{-c|y|^2}\).
The exponent remainder \(O(N^{-1/2}|y|^3)\) is \(o(1)\) there;
the retained remainder bound is a Gaussian polynomial, so summing
its square costs only \(O(N^{\ell/2})\), without a power loss.
The intermediate tail is smaller than every algebraic order by
the negative local Hessian. The compact global gap and uniform
endpoint factorial bound control all other entries exponentially.
A fixed rescaled ball supplies the matching norm lower bound.
This proves the first part of (14). For \(J=1\), its relative
error is \(O(N^{-1})\); the order-\(N^{-1/2}\) squared correction
is odd. Gaussian-polynomial mesh sums have exponentially small
errors uniformly in their fractional centers, by periodization and
the Gaussian Fourier integral as in [G]. This proves the second
part of (14), including all parity and rounding shifts.

## 5. A degree-\(r\) optimizer for an entire donor-tilt chamber

Multiply the input column with donor index \(a\) by \(e^{\eta a}\),
where \(\eta\) is any fixed real number. This is (12)'s direction
\(\lambda=\eta(1,\boldsymbol1,\boldsymbol0)\). Formula (5) reduces
the whole maximization exactly to \(I_r(A)+\eta A\), \(0\le A\le1\).
Put \(m=2r+1\). The function \(u\cot u\) strictly decreases on
\((0,\pi)\): its derivative has numerator \(\sin u\cos u-u<0\).
Consequently

\[
 I_r''(A)=\pi\cot(\pi A)-{\pi\over m}\cot(\pi A/m)<0,\quad
 I_r'(0+)=\log m,\quad I_r'(1-)=-\infty.
 \tag{16}
\]

There is a unique interior maximizer \(A_\eta\) precisely when
\(\eta>-\log m\). It solves
\(\sin(\pi A_\eta)/\sin(\pi A_\eta/m)=e^{-\eta}\).
For \(\eta\le-\log m\) the maximum is \(A=0\), with value zero;
no interior Gaussian assertion is made there.
Writing \(\theta=\pi A_\eta/m\), the interior optimizer is
\(x=\theta/\pi\), \(t_i=2\theta/\pi\),
\(v_i=1/2-\theta/\pi\), and is determined by the single polynomial

\[
 P_r(y)=e^{-\eta},\qquad
 P_r(y)=U_{2r}(\sqrt y)
   =4^r\prod_{j=1}^r\left(y-\cos^2{j\pi\over m}\right),
 \quad \cos^2(\pi/m)<y=\cos^2\theta<1.
 \tag{17}
\]

Here \(U_0(z)=1,U_1(z)=2z\), and
\(U_{j+1}(z)=2zU_j(z)-U_{j-1}(z)\), define the Chebyshev
polynomials of the second kind. The sine identity for \(U_{2r}\)
proves (17); its paired roots and leading coefficient give the
product, and the recurrence proves integer coefficients.
On the displayed interval every factor is
positive and strictly increasing, so \(P_r\) increases from zero
to \(m\). Its degree is \(r\), independently of \(N\).
For example \(P_1=4y-1\), \(P_2=16y^2-12y+1\).
This is the explicit fan norm optimizer, not a knot \(A\)-polynomial.

For the full Hessian, put
\(\alpha=\pi\cot\theta,\ \beta=\pi\tan\theta,\
\gamma=\pi\cot(m\theta)\). Its \(x,t\) block is
\(\operatorname{diag}(\alpha,(\alpha+\beta)I/2)
-\gamma\boldsymbol1\boldsymbol1^{\mathsf T}\);
the \(v\) block is \(2\beta I\) and its only cross block is
\(H_{tv}=\beta I\). Eliminating \(v\) leaves
\(\operatorname{diag}(\alpha,\alpha I/2)
-\gamma\boldsymbol1\boldsymbol1^{\mathsf T}\).
This is positive definite since \(\alpha-m\gamma>0\), by (16), and

\[
 \det H_\eta=\pi^{2r+1}\{\cot\theta-m\cot(m\theta)\},\qquad
 A(z_\eta)^2=e^{-\eta}\sin(2\theta)^{-r}.
 \tag{18}
\]

The second formula follows from (10) and the stationary sine ratio.
The determinant follows from the one rank-one Schur block.
Thus, writing \(M_\eta=I_r(A_\eta)+\eta A_\eta\),

\[
 \|\mathsf F_{r,N,\eta}\|_{\rm HS}^2
 =\sqrt N\,e^{2NM_\eta}
 {e^{-\eta}(2\sin2\theta)^{-r}\over
          \sqrt{\cot\theta-m\cot(m\theta)}}(1+O(N^{-1})).
 \tag{19}
\]

The packet estimate (14) holds uniformly over every fixed compact
subinterval of \(\eta>-\log m\), also allowing sufficiently small
full boundary perturbations there. Indeed these maxima stay uniformly
interior, (18) gives positive Hessians, and compactness preserves the
global gap. The proof of (14) then applies unchanged. No geometric
interpretation of this entire donor-tilt chamber is asserted.

## 6. An independently specified product boundary coefficient

The following is an actual open coefficient, rather than an unknown
boundary state supplied as input. Let \(L_{\rm in},L_{\rm out}\)
be the fixed integer matrices sending \(n\) to the input and output
lists in (3), and stack them as \(L\). This matrix has full column
rank: its input list contains every \(b_i\), its output contains
\(d\), and \(k_i=\mathrm{out}_i-b_i\). Set
\(\nu_{\rm in}=L_{\rm in}z_*\),
\(\nu_{\rm out}=L_{\rm out}z_*\); all these coordinates lie
strictly between zero and one.

Choose the real quadratic lift \(\Theta_N(n)\) of (3)'s phase
using \(\arg\kappa=\pi D^2/(2N)\),
\(\log x_0=i(\pi-\pi/N)\), and \(\arg(-i)=-\pi/2\).
Thus \(e^{i\Theta_N(n)}=\Xi_N(n)\) at every integer state and
\(C=N\Theta_N''\) is a fixed real symmetric matrix.
Choose real per-head carriers satisfying

\[
 L_{\rm in}^{\mathsf T}\theta_{\rm in}
       -L_{\rm out}^{\mathsf T}\theta_{\rm out}
                      =-\nabla\Theta_N(Nz_*).
 \tag{20}
\]

There is an explicit choice. If the right-hand gradient before its
minus sign is \(g=(g_x,\boldsymbol g_t,\boldsymbol g_v)\), take
\(\theta_{\rm in,0}=0,\ \theta_{\rm out,0}=g_x,\
\theta_{\rm out,i}=g_{t_i},\
\theta_{\rm in,i}=g_{t_i}-g_{v_i}\).
Every coefficient is known from \(r,N\), independently of a tangle
or a closed source.

For each coordinate \(\nu,\theta\), define a unit head vector

\[
 \psi_{\nu,\theta,N}(j)
 ={e^{-(j-N\nu)^2/(2N)+i\theta(j-N\nu)}\over Z_{\nu,N}},
 \qquad Z_{\nu,N}^2=\sum_{j=0}^{D}e^{-(j-N\nu)^2/N}.
 \tag{21}
\]

Tensor these vectors with the indicated input/output data to form
\(\Psi_{\rm in,N}\), \(\Psi_{\rm out,N}\). Then

\[
 \boxed{\quad
 \langle\Psi_{\rm out,N},\mathsf F_{r,N}\Psi_{\rm in,N}\rangle
 =e^{NM_r+i\Theta_N(Nz_*)}
 {2^{(r+1)/2}\pi^{r/2}A_*\over
           \sqrt{\det(H+L^{\mathsf T}L-iC)}}
                         (1+O_r(N^{-1/2})).
 \quad}
 \tag{22}
\]

The square root is continued from \(C=0\) inside the accretive
complex symmetric matrices, equivalently fixed by the Gaussian
integral. Its denominator is nonzero, since the matrix has real part
\(H+L^{\mathsf T}L>0\).
To prove the formula, each normalizer in (21) is
\((\pi N)^{1/4}(1+O(e^{-cN}))\), uniformly in its fractional center.
The two tensor boundaries contribute \((\pi N)^{-(r+1)/2}\).
Equation (20) cancels the exact phase gradient; the remaining phase
is exactly \(\Theta_N(Nz_*)+y^{\mathsf T}Cy/2\).
The Gaussian product supplies \(e^{-y^{\mathsf T}L^{\mathsf T}Ly/2}\).
Insert (13) at order zero and use the Gaussian-polynomial error
estimate just proved, now in the scalar sum. Its mesh contributes
\(N^{\ell/2}\), its entry density \((2N)^{-r/2}\), and its integral
\((2\pi)^{\ell/2}/\sqrt{\det(H+L^{\mathsf T}L-iC)}\).
The powers of \(N\) cancel. The complex Gaussian mesh sum has the
same convergence: its Fourier transform is Gaussian and the inverse
matrix has positive real part. The same tail bounds apply with the
additional Gaussian factors of modulus at most one. This proves
(22) with a relative error, because its fixed leading constant is
nonzero. It proves no assertion about prescribed knot boundary data.

## 7. Negative fans, interfaces, and the original closing

There is a simple flat-metric negative version. In the same order
put \(\mathsf F^-_{r,N}=R_r^-\cdots R_1^-\). Its input/output
path is \((a,\boldsymbol b)\mapsto
(b_1-k_1,\ldots,b_r-k_r,a+K_r)\), with \(k_i\le b_i\) and
\(a+K_r\le D\). Its modulus is
\(s_{a+K_r}/s_a\prod_i s_{b_i}/(s_{b_i-k_i}s_{k_i})\).
Complement every input and output index by \(j\mapsto D-j\).
The reflection \(s_j s_{D-j}=N\) identifies this modulus exactly
with (3)'s positive modulus on the complemented support. Keep the
negative word's own product phase from [G, (6)]. This gives the same
flat norm (11) and all-order packet estimate by an entry bijection;
no unproved symmetry or inverse approximation is used. Formula (22)
was stated only for the positive fan.

The tilts in (12) are actual diagonal gauges. Undoing them can cost
exponentially in \(N\); both incident interface factors, original
pivots and normalization budgets must remain. These estimates do not
identify the tilted maximum with arbitrary geometric Conway data.
They describe one fixed fan, not a word with repeated arbitrary
crossings, arbitrary signs, or an expression growing with \(N\).
The arrays retain the literal full finite head spaces, without a
semisimple value quotient. No uniform meridian- or quantum-normal
derivative estimate is inferred from the root-level packet theorem.

In particular the prepared vectors in (22) are not the original
closing. For the usual first-head cut and pivotal tail traces of
this braid, the tail support equations include
\(b_i=b_{i+1}+k_{i+1}\) for \(i<r\), and \(b_r=d\).
For \(r\ge2\) the flat maximum (6) does not satisfy them.
Replacing the globally scalar knot cut by a trace-one probe does not
remove these internal equations. No scalar geometric lower bound or
finite-exception volume theorem follows from this open-fan result.

## Complete inputs and coverage

All four complete matching texts were read. [G] supplies the actual
entry and fixed-order factorial estimates; all fan optimizations,
determinants, prefactors and product probes are derived above.
[W] already proves the one-crossing physical weighted norm rate.
[B] already has the same regular bipyramid value for a fused Fourier
bridge, whose clocks are not termwise physical occupation indices.
[D] already proves a nonzero finite factorial-donor coherent kernel
on its stated lower-donor scale. Neither is replaced by or claimed
to be the joint uniform-physical fan coefficient (22).

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| G, direct, 306 lines | [Whole physical crossing packet](research_full_physical_crossing_gaussian_packet.md) | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| W, coverage, 244 lines | [Weighted complete crossing](weighted_crossing_source_gap.md) | a6a6411a780c904493db4fca3b5536f902aa5be8b6ef7cfb880a4f57509f436c |
| B, coverage, 301 lines | [Role frames and bridge angles](research_rivin_role_frames_and_bridge_angles.md) | 125155bcd008e24bf5714457d9c6d1788a152bc563380f859c80bfe8b997ccf8 |
| D, coverage, 392 lines | [Finite donor coherent sum](research_reduced_euler_donor_coherent_sum.md) | ff35583f203ae7686de4ff7fb91fcb4d4d0190e4f8995bd89a871849bc91d7f4 |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical test, build, git operation or
earlier-final edit was performed.
