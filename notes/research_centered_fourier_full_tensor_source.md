# Closed products and Gaussian weights for the full Conway tensor

Written research proof, 22 November 2026.

The generating polynomial of the entire centered Conway tensor has a
single finite sum over the physical Casimir nodes. Every summand uses
explicit finite products and a quadratic Gaussian crossing weight.
The first-normal contribution is explicit as well. In particular this
does not replace the repeated-root algebra by its ordinary values.

The result generates all three-index coefficients algebraically and
gives a uniform complex upper bound for their generating polynomial on
fixed discs. It does not estimate their coherent contraction with a
short component or prove an action-relative geometric bound.

## 1. The polynomial generating the centered modes

Fix the original level and phases
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 h=Q^{-1},\quad \eta=(-1)^d,\quad \kappa=q^{d^2/2},
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal H_N=\mathbb C[z]/(P_N).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
Every fractional power of \(q\) means its displayed exponential.
Use the original Frobenius trace \(\phi_N\) and centered basis \(f_a\)
of the Fourier compiler. Its signed crossing class \(R=R^+\) obeys
\[
 f_a=N^{-1/2}R\,p_a(z),\qquad p_0=1,\qquad
 C_{abc}=\phi_N(f_af_bf_c).
 \tag{2}
\]
Each \(p_a\) is its unique ordinary polynomial of degree \(a\).
The entire quotient, including its spectral first normals, is used.

Define an ordinary polynomial in independent variables \(t,z\):
\[
                         A_N(t,z)=\sum_{a=0}^d p_a(z)t^a.
 \tag{3}
\]
It satisfies the exact forced equation
\[
 \boxed{\quad
 (1+zt+t^2)A_N(t,z)
       -(1+q^{-1}t)^2A_N(ht,z)
                      =\frac{\eta}{N}P_N(z)t^N.
 \quad}
 \tag{4}
\]
This is an ordinary polynomial identity, not just an identity at
distinct spectral values.

Here is its derivation. The compiler gives
\[
 zp_a=(h^{a+1}-1)p_{a+1}
             +2q^{-1}h^ap_a+(h^a-1)p_{a-1},
 \qquad p_{-1}=0,\quad 0\le a<d.
 \tag{5}
\]
The final equation at \(a=d\) holds in \(\mathcal H_N\), with its
first term absent since \(h^N=1\). Sum these equations after
multiplication by \(t^{a+1}\). All coefficients of the difference
in (4) vanish except possibly that of \(t^N\); the \(t^{N+1}\)
coefficient cancels because \(h^N=1\).
The remaining coefficient vanishes in the full quotient and has
degree at most \(N\) in \(z\), hence is a scalar multiple of \(P_N\).
By (5),
\[
 [z^a]p_a=\frac{(-1)^a}{(h;h)_a},\qquad (h;h)_d=N.
 \tag{6}
\]
Its leading coefficient is therefore \(\eta/N\), proving (4).

We will repeatedly use coefficientwise uniqueness in \(t\).
For a polynomial \(X(t)\) of degree at most \(d\), its constant term
and the right side of (4) determine every other coefficient: in degree
\(t^a\), \(1\le a<N\), the coefficient of the new unknown is
\(1-h^a\ne0\). The remaining terms involve only lower degrees.
This argument also applies to the differentiated inhomogeneous
equations below.

## 2. Closed products at every physical node

Index the distinct physical nodes by
\[
 0\le j\le\lfloor d/2\rfloor,\qquad
 \theta_j=(2j+1)\pi/N,\quad v_j=qQ^j=e^{i\theta_j},\quad
 c_j=v_j+v_j^{-1},\quad m_j=N-2j-1.
 \tag{7}
\]
The double nodes have \(m_j>0\), equivalently
\(0\le j\le\lfloor(N-2)/2\rfloor\).
When \(N\) is odd, the last node \(j_*=(N-1)/2\) is simple:
\(c_{j_*}=-2\) and \(m_{j_*}=0\).

Use empty products when an interval has length zero, and define
\[
 D_j(t)=\prod_{r=-j+1}^{0}(1+q^{-1}Q^rt),\qquad
 B_j(t)=\prod_{r=j+2}^{N-j}(1+q^{-1}Q^rt).
 \tag{8}
\]
Their degrees are \(j\) and \(m_j\), respectively. The exponent \(r=N\)
in a product means \(Q^N=1\); no endpoint factor is omitted.
Then the exact physical value of the whole generating polynomial is
\[
 \boxed{\qquad A_N(t,c_j)=D_j(t)^2B_j(t).\qquad}
 \tag{9}
\]
Thus all values \(p_a(c_j)\) are coefficients of one finite product.

To prove (9), call its proposed right side \(V_j(t)\).
Cancellation of its consecutive factors gives
\[
 \frac{D_j(ht)}{D_j(t)}
       =\frac{1+q^{-1}Q^{-j}t}{1+q^{-1}t},\qquad
 \frac{B_j(ht)}{B_j(t)}
       =\frac{1+q^{-1}Q^{j+1}t}{1+q^{-1}Q^{-j}t}.
 \tag{10}
\]
For the empty last product at an odd simple node, the numerator and
denominator in its displayed ratio coincide. Since
\(q^{-1}Q^{j+1}=v_j\) and \(q^{-1}Q^{-j}=v_j^{-1}\), (10) gives
\[
 (1+c_jt+t^2)V_j(t)=(1+q^{-1}t)^2V_j(ht).
 \tag{11}
\]
Ratios here may first be read off their zero sets; after clearing
denominators they are polynomial identities everywhere.
The degree of \(V_j\) is \(2j+m_j=d\), and \(V_j(0)=1\).
Equation (4) is homogeneous at \(z=c_j\), so the uniqueness just
proved gives (9). No infinite-product specialization is involved.

## 3. The full first normal

At every double node the required normal is
\[
 \boxed{\qquad
 \partial_z A_N(t,c_j)
       =\frac{D_j(t)^2\,tB_j'(t)}{v_j-v_j^{-1}}.
 \qquad}
 \tag{12}
\]
Here the prime on \(B_j\) means differentiation in \(t\).
The formula is a spectral derivative in \(z\), not the result of
differentiating (9) in a continuously varied index \(j\).
No derivative condition is imposed at the odd simple node.

Differentiate (4) in \(z\). At a double node \(P_N'(c_j)=0\), giving
\[
 (1+c_jt+t^2)\partial_zA_N(t,c_j)
       -(1+q^{-1}t)^2\partial_zA_N(ht,c_j)
                          =-tA_N(t,c_j).
 \tag{13}
\]
The proposed right side of (12) is polynomial of degree at most \(d\)
and has constant term zero. To verify (13), put
\[
 L_j(t)=\frac{tB_j'(t)}{B_j(t)}
       =\sum_{r=j+2}^{N-j}
                   \frac{q^{-1}Q^rt}{1+q^{-1}Q^rt}.
\]
The two ends of this finite sum give
\[
 L_j(t)-L_j(ht)
  =\frac1{1+v_jt}-\frac1{1+v_j^{-1}t}
  =-\frac{(v_j-v_j^{-1})t}{1+c_jt+t^2}.
 \tag{14}
\]
Multiply (14) by the product identity (11). The result is precisely
(13) for (12), first where the rational expressions are defined,
then everywhere as a polynomial identity. Coefficientwise uniqueness
with constant term zero proves the full normal formula.
The denominator \(v_j-v_j^{-1}=2i\sin\theta_j\) is nonzero at every
double node, including the last even-level double node.

For example \(N=2\) gives
\[
 A_2(t,z)=1+(-z/2-i)t,\quad
 D_0=1,\quad B_0=1-it,\quad
                  \partial_zA_2(t,0)=-t/2 .
 \tag{15}
\]
At \(N=3\), the simple node has
\(A_3(t,-2)=(1+q^{-1}t)^2\); its derivative is not needed.

## 4. The literal trace and Gaussian crossing data

For a germ \(F\) at the physical nodes the original full trace is
\[
 \phi_N(F)=\eta\sum_{j\ {\rm double}}
          \{(4-c_j^2)F'(c_j)-c_jF(c_j)\}
                   +\mathbf1_{N\ {\rm odd}}F(-2).
 \tag{16}
\]
We recall its normalization. The top Newton polynomial has leading
coefficient \(\eta/N^2\) and trace one. Therefore \(\phi_N\) is
\(\eta N^2\) times the leading coefficient of the full Hermite
remainder. That coefficient is the sum of the finite residues of
\(F/P_N\). At a double root the Chebyshev equation gives
\[
 \frac{P_N''(c_j)}2=\frac{N^2}{4-c_j^2},\qquad
 \frac{P_N'''(c_j)}{3P_N''(c_j)}=\frac{c_j}{4-c_j^2}.
 \tag{17}
\]
The residue is thus
\(\{(4-c_j^2)F'(c_j)-c_jF(c_j)\}/N^2\).
At the odd simple node \(P_N'(-2)=N^2\) and \(\eta=1\).
This proves (16), retaining all required first normals.

Use the original signed positive crossing, not a fitted Gaussian.
Its value and its independent full normal are
\[
 \rho_j:=R(c_j)=\kappa(-1)^jq^{j(j+1)},\qquad
 \frac{R'(c_j)}{R(c_j)}
                    =\frac{i\,m_j}{4\sin\theta_j}
                         \quad(j\ {\rm double}).
 \tag{18}
\]
These are the literal full-jet crossing formulas in the phase-transport
source. They follow there by checking the holomorphic representative
\[
 q^{d^2/4}\exp\!\left(\frac{iN}{4\pi}
                             \arccos(-z/2)^2\right)
 \tag{19}
\]
at the physical angular lifts and differentiating it in \(z\).
Its square-angle branch is regular at \(-2\) and slit at \([2,\infty)\).
The first normal is part of the source identity, not inferred from the
values in (18). At the odd simple node use only the value \(\rho_{j_*}\)
in (18)'s first formula. Every \(\rho_j\) has modulus one.

## 5. One finite Gaussian sum for all coefficients

Let \(\mathbf t=(t_1,t_2,t_3)\), and put
\[
 \mathscr C_N(\mathbf t)=\sum_{a,b,c=0}^d
                                  C_{abc}t_1^at_2^bt_3^c.
 \tag{20}
\]
Equations (2)--(3) give the exact full-algebra identity
\[
 \mathscr C_N(\mathbf t)
       =N^{-3/2}\phi_N\!\left(R^3
                         \prod_{\ell=1}^3 A_N(t_\ell,z)\right).
 \tag{21}
\]
Substitute (9), (12), and (18) into the literal trace (16). The result is
\[
 \boxed{\begin{aligned}
 \mathscr C_N(\mathbf t)
 ={}&\frac{\eta}{N^{3/2}}\sum_{j\ {\rm double}}
     \rho_j^3\prod_{\ell=1}^3D_j(t_\ell)^2\\
 &\ \cdot\left[
 (3im_j\sin\theta_j-c_j)\prod_{\ell=1}^3B_j(t_\ell)
 -2i\sin\theta_j\sum_{\ell=1}^3
       t_\ell B_j'(t_\ell)\prod_{r\ne\ell}B_j(t_r)
          \right]\\
 &+\frac{\mathbf1_{N\ {\rm odd}}}{N^{3/2}}\,
       \rho_{j_*}^3\prod_{\ell=1}^3D_{j_*}(t_\ell)^2 .
 \end{aligned}}
 \tag{22}
\]
The sum has one term per distinct physical node. All factors in its
products are explicit in (8). The crossing weight
\(\rho_j^3=\kappa^3(-1)^jq^{3j(j+1)}\) is a specified quadratic
Gaussian phase. Its normal contributes the term
\(3im_j\sin\theta_j\); omitting it would change the tensor.
The normal of \(A_N\) differentiates the \(B_j\) factor as in (12),
and is exactly the other term in the bracket.

The odd simple node has its own coefficient one in (16), rather
than being inserted into a double-node formula with a singular
denominator or an extra factor two. In particular the constant
terms of (22) at \(N=2,3\) are respectively
\[
              C_{000}=\frac{3\kappa}{2\sqrt2},\qquad
              C_{000}=\frac{-2+3i\sqrt3}{3\sqrt3}.
 \tag{23}
\]
These also follow directly from
\(C_{000}=N^{-3/2}\phi_N(R^3)\).

Equation (22) is an identity of trivariate ordinary polynomials.
Coefficient extraction gives every \(C_{abc}\), with all phase carriers
and both level parities. It is not an evaluation restricted to
distinct spectral roots: the separately proved normal formula is
essential to that statement.

## 6. An explicit cyclic rank-one equation

The finite forcing also determines the exact cyclic compatibility
condition. Put \(a=q^{-1}\) and
\[
 g(t,z)=\frac{1+zt+t^2}{(1+at)^2}.
\]
In the rational function ring with polynomial \(z\), one has
\[
 \boxed{\quad
 \prod_{r=0}^{N-1}g(h^rt,z)
 =1-\frac{(-1)^NP_N(z)t^N}
                  {[1+(-1)^Nt^N]^2}.
 \quad}
 \tag{24}
\]
For an elementary proof introduce \(v\) with \(v+v^{-1}=z\).
The numerator product is
\[
 (1-(-vt)^N)(1-(-v^{-1}t)^N)
   =1-(-1)^N(P_N(z)-2)t^N+t^{2N},
\]
using \(v^N+v^{-N}=2T_N(z/2)=P_N(z)-2\).
The denominator is
\((1-(-at)^N)^2=[1+(-1)^Nt^N]^2\), since \(a^N=-1\).
Subtracting these two expressions proves (24); their symmetric
dependence on \(v,v^{-1}\) makes it a polynomial identity in \(z\).

This gives a precise cyclic statement on the nonreduced algebra.
Let
\[
 \mathcal B=\mathcal H_N\otimes_{\mathbb C}\mathbb C(t),\qquad
 \sigma(t)=ht,\quad \sigma(z)=z.
\]
Then \(\mathcal B^\sigma=\mathcal H_N\otimes\mathbb C(t^N)\):
expand in a fixed complex basis of \(\mathcal H_N\), and then use
the basis \(1,t,\ldots,t^{N-1}\) of \(\mathbb C(t)\) over
\(\mathbb C(t^N)\), on which \(\sigma\) acts diagonally with
distinct eigenvalues \(1,h,\ldots,h^{N-1}\).
By (24) the cyclic product of \(g\) is one in \(\mathcal B\), and
(4) reads
\[
                  \sigma A_N=gA_N\quad\hbox{in }\mathcal B.
 \tag{25}
\]
The element \(A_N\) is invertible there. Indeed (9) is a nonzero
rational function at every residue field of \(\mathcal H_N\);
an element of each dual-number component is a unit exactly when
its value is nonzero. Thus the set of invertible solutions of (25)
is nonempty, and every such solution is uniquely \(A_N b\) with
\(b\in(\mathcal B^\sigma)^\times\). This follows just by taking
the ratio of two solutions. It requires no general Hilbert 90
theorem over a nonreduced ring.

Among polynomial solutions of degree less than \(N\) in \(t\),
the normalization \(A_N(0,z)=1\) selects this one by the
coefficientwise uniqueness following (6). In particular the cyclic
description retains the nilpotent components rather than taking
the norm only at distinct spectral values.

## 7. A uniform complex bound for the full generating tensor

Fix \(0<r<1\). Define the dilogarithm only on its convergent disc,
\(\operatorname{Li}_2(w)=\sum_{k\ge1}w^k/k^2\), and set
\[
 \mathcal S(v,t)=
 \frac{\operatorname{Li}_2(-vt)+\operatorname{Li}_2(-v^{-1}t)
                           -2\operatorname{Li}_2(-t)}{2\pi i},
 \qquad |v|=1,\quad |t|\le r.
 \tag{26}
\]
Every factor in (9) is zero-free on this disc. With logarithms
normalized to zero at \(t=0\), one has the uniform estimate
\[
             \log A_N(t,c_j)=N\mathcal S(v_j,t)+O_r(1),
       \qquad |t|\le r,
 \tag{27}
\]
simultaneously for every physical node, every \(N\ge2\), and both
parities.

Here the complex logarithm, not just its real part, is controlled.
Write \(f_t(u)=\log(1+te^{iu})\). Its size and first derivative
are uniformly bounded for \(|t|\le r\). The consecutive factors
in (8), whose phase spacing is \(2\pi/N\), give Riemann sums
with a uniformly bounded total error. Their endpoints differ by
at most a fixed number of mesh cells from the arcs
\([-\theta_j,0]\) and \([\theta_j,2\pi-\theta_j]\). Hence
\[
 \frac1N\log(D_j(t)^2B_j(t))
 =\frac1{2\pi}
     \left(2\int_{-\theta_j}^0 f_t(u)\,du
             +\int_{\theta_j}^{2\pi-\theta_j} f_t(u)\,du\right)
       +O_r(N^{-1}).
\]
The full circle integral is zero, by the absolutely convergent
logarithm series. The displayed integral therefore equals
\((2\pi)^{-1}(\int_{-\theta_j}^0-\int_0^{\theta_j})f_t\).
Integrating the same series identifies it with (26). This proves
(27), including shrinking arcs at the end nodes.

The normal is controlled uniformly as well:
\[
       \left|\frac{\partial_zA_N(t,c_j)}{A_N(t,c_j)}\right|
                         \le C_rN\quad(j\ {\rm double}).
 \tag{28}
\]
For completeness, the logarithmic derivative \(L_j=tB_j'/B_j\)
is bounded by \(C_r m_j\). Taking instead the complementary
factors in the full length-\(N\) product gives the second bound
\[
 |L_j|\le C_r(N-m_j)+C_rNr^N.
\]
The last term comes from the logarithmic derivative of
\(\prod_{s=1}^N(1+q^{-1}Q^st)=1+(-1)^Nt^N\).
Now
\(\min(m_j,N-m_j)=N\min(\theta_j,\pi-\theta_j)/\pi\)
and
\(\min(\theta_j,\pi-\theta_j)/\sin\theta_j\le\pi/2\).
Also \(\sin\theta_j\ge2/N\) at double nodes, while
\(Nr^N\) is uniformly bounded. Divide these estimates by
\(|v_j-v_j^{-1}|=2\sin\theta_j\) and use (12) to get (28).

Combining the original trace with (27)--(28) gives an actual
upper bound for the whole tensor-generating polynomial:
\[
 \boxed{\quad
 |\mathscr C_N(t_1,t_2,t_3)|
 \le C_rN^{1/2}
   \exp\!\left\{N\max_{0\le j\le\lfloor d/2\rfloor}
           \operatorname{Re}\sum_{\ell=1}^3
                         \mathcal S(v_j,t_\ell)\right\},
       \qquad |t_\ell|\le r.
 \quad}
 \tag{29}
\]
Indeed each double-node summand of (21) has modulus at most
\(C_rN\prod_\ell|A_N(t_\ell,c_j)|\): in (16), the
crossing normal contributes
\((4-c_j^2)3|R'/R|=3m_j\sin\theta_j\le3N\),
the other three normals are bounded by (28), and \(|c_j|\le2\).
The simple-node term obeys the same safe bound. There are at most
\(N\) nodes and the prefactor is \(N^{-3/2}\), proving (29).
All constants depend only on the fixed disc radius.

The estimate is uniform on fixed complex discs inside the unit
disc. It does not assert a bound as \(r\) tends to one, a lower
bound on an individual coefficient, or an identification of its
variational exponent with a geometric filling action.

## 8. Scope and complete sources

The three-index Fourier calculation has been replaced by one physical
node sum of closed products and their specified polynomial derivatives.
There is no unknown source coefficient in (22).
This is not a low-rank replacement of the \(N\)-dimensional boundary
algebra; the generating polynomial still contains all \(N^3\) tensor
coefficients. The original turns, bilinear gluing and marked closure
remain those of the centered compiler.

No positive measure is assigned to the Gaussian-weighted node sum.
No individual-entry asymptotic, geometric norm, source-cycle estimate,
or new volume-conjecture class is inferred. The valid complex bound
(29) takes absolute values of the node terms and is not claimed to
retain their cancellations or be sharp.
All derivatives here are the original spectral Hermite normals;
no moving-\(q\) or peripheral-normal extension is asserted.

The two complete matching proof sources are:

| Source | SHA-256 |
|---|---|
| [Centered Fourier compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Original Hermite phase transport and trace, 293 lines](research_bergman_jet_quotient_phase_transport.md) | 0985159d134d82a404bd07973cf5ee55eb78c115e154465cbeac1b201c1c2686 |

The finite forcing, cyclic equation, value product, spectral normal,
generating formula and fixed-disc bound are proved above. No
generic-parameter orthogonality measure, infinite product, or
hypergeometric summation theorem is imported.
For coverage, the generic Al-Salam--Chihara generating function is
standard: see Dennis Stanton,
[Generating functions and orthogonality (2022), equation (2.1)](https://www-users.cse.umn.edu/~stant001/PAPERS/Dick-gf2022.pdf).
The compiler's normalization is
\(p_a(z)=(-1)^a Q_a(z/2;q^{-1},q^{-1}\mid h)/(h;h)_a\),
so the usual generic series uses the variable \(-t\).
This reference is coverage of that generic generating function only.
No infinite product at a root of unity or external orthogonality
argument is used for the finite forced equation or its full-normal
source formulas.
Earlier finals and public manuscripts remain unchanged.
