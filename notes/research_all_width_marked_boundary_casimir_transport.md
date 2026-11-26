# Explicit boundary Casimirs in the marked observation coordinates

24 November 2026. Written research proof.

The all-width marked observation has an explicit inverse on the actual
source. This note replaces that full reconstruction, for each of the two
outer pair Casimirs, by one shared linear Borel resolvent on the middle
physical packet. All other pair Casimirs remain literal middle operators.
The resolvent has an exact finite inverse with denominator two, at every
level, and norm at most \(e^{C_bN}\) at fixed width. In a specified
coherent Borel metric its normalized multiplier has norm at most three.

The formulas transport the actual braid representation by its original
Casimir polynomials, including every Jordan derivative. The braid
polynomials themselves are not asserted to have bounded order. All
source constraints remain, and the original marked closing has an
explicit physical row with polynomial norm. These
identities do not lower-bound the final coherent scalar.

## 1. Source, middle packet and statement

Fix \(N\ge2\), and use the complete conventions of [O,M,P]:
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad \xi=q^{-3},\quad \theta=\pi/(2N).
 \tag{1}
\]
On the original orthonormal physical head \(V=\mathbb C^N\),
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle .
 \tag{2}
\]
Missing arrows are zero. The coproducts are
\[
 E_{12}=E_1K_2+E_2,\qquad
 F_{12}=F_1+K_1^{-1}F_2,\qquad K_{12}=K_1K_2 .
 \tag{3}
\]
The unrolled weight \(H|a\rangle=(d-2a)|a\rangle\) is additive.
The actual unscaled pair Casimir is
\[
 \Omega_{12}=F_{12}E_{12}+qK_{12}+q^{-1}K_{12}^{-1}.
 \tag{4}
\]
In particular the one-head scalar identity is
\(FE+qK+q^{-1}K^{-1}=-2I\).

Let \(b\ge4\) be even, \(n=b-2\), and \(W=V^{\otimes n}\).
Write \(E,F,K\), without a subscript, for the total operators on \(W\).
Write \(E_j,F_j,K_j\) for its individual physical heads.
The original endpoint rows and observation are
\[
 \eta_a=\frac{1-q^3}{2}q^{3a},\qquad
 \zeta_a=\frac{1-q^{-3}}2x^a,\qquad
 \mathscr D=\eta\otimes I_W\otimes\zeta .
 \tag{5}
\]
As in [O], let \(\mathcal I_b\) be the full unrolled root invariant
space and \(\mathcal S_b\) its saturated generic source subspace.
Their images under \(\mathscr D\) retain [O]'s unrolled and
divided-current equations.

It is useful to state the larger working domain as well. Let
\(\mathcal I_b^{\rm sm}=\ker E_{\rm tot}\cap\ker F_{\rm tot}
\cap\ker(K_{\rm tot}-I)\), without the unrolled condition.
The same literal currying and Borel reconstruction in [O] identify
\[
 \mathcal K_W:=\mathscr D(\mathcal I_b^{\rm sm})
       =\ker(B_\sigma^W-\sigma I),\qquad
 B_\sigma=F-EK^{-1}+\sigma K^{-1},\quad
 \sigma=-q^{-1}-q^2 .
 \tag{6}
\]
The smaller actual source image is
\(\mathcal Y_b=\mathscr D(\mathcal S_b)\subset\mathcal K_W\).
Neither the unrolled nor the generic-source constraint follows
just from membership in \(\mathcal K_W\).

Define operators on the whole middle physical space:
\[
 \mathcal C=E-\xi K,\qquad
 \mathcal R=(\mathcal C+QI)^{-1},\qquad
 \mathcal V=(1-\xi)\mathcal R .
 \tag{7}
\]
The inverse in (7) always exists; it is proved below.
Set
\[
 \begin{split}
 C_{L,0}&=-2K_1+q^3E_1-q^{-4}F_1K_1,\\
 C_{L,+}&=(1+q^{-2})K_1-q^3E_1
                              +q^{-6}F_1K_1+2q^{-1}I,\\
 C_{R,0}&=qF_n-K_n^{-1}E_n-2K_n^{-1},\\
 C_{R,+}&=2qI+(1+q^2)K_n^{-1}-q^3F_n+K_n^{-1}E_n .
 \end{split}                                                   \tag{8}
\]
All products have the displayed order. In particular \(K_n^{-1}E_n\)
has not been interchanged.

**Theorem.** The transported pair Casimirs are the restrictions of
the following explicit operators on \(W\):
\[
 \boxed{\quad
 T_1=C_{L,0}+C_{L,+}\,QK\mathcal V,\qquad
 T_{b-1}=C_{R,0}+C_{R,+}\mathcal V,\qquad
 T_i=\Omega^W_{i-1,i}\quad(2\le i\le b-2).
 \quad}                                                        \tag{9}
\]
For every \(\Phi\in\mathcal I_b^{\rm sm}\),
\[
                 T_i\mathscr D\Phi
                         =\mathscr D\Omega_{i,i+1}\Phi .
 \tag{10}
\]
They consequently preserve \(\mathcal K_W\), the unrolled image,
and the actual saturated source image \(\mathcal Y_b\).
For fixed \(b\), on the whole physical \(W\),
\[
       \|\mathcal R\|+\|\mathcal V\|+\|T_1\|+\|T_{b-1}\|
                                                     \le e^{C_bN}.
 \tag{11}
\]
No polynomial bound on these physical norms is asserted.
The shared auxiliary vector \(\mathcal V y\) need not belong
to any of the constrained source images.

## 2. Literal currying and the two cup transposes

Retain the original turns
\[
 p_{ab}=Nx^{-b}\delta_{a+b,d},\qquad
 \ell_{ab}=x^a\delta_{a+b,d}/N,\qquad
 m_{ab}=x^b/N^2 .
 \tag{12}
\]
There is no degree delta in \(m\).
Let \(P=(p_{ab})\), and let \(A=V\otimes V\) be the two-input
module for the literal currying
\[
 \Phi_f=(I\otimes f\otimes I)(p_{12}\otimes p_{34}),\qquad
 f:A\longrightarrow W .
 \tag{13}
\]
For small Hopf intertwiners, this is exactly the invariant
tensor correspondence, with no unrolled equation imposed.
Adding the unrolled equation gives [O]'s original \(\mathcal I_b\).
Its entrywise normalization is
\[
 (\Phi_f)_{a,i,b}
       =N^2x^{a-b-d}f_{i,d-a,d-b},\qquad
                         \|\Phi_f\|_{\rm ph}=N^2\|f\|_{\rm HS}.
 \tag{14}
\]

The observation is evaluation at the fixed pair vector
\[
 y=\mathscr D\Phi_f=f(\mathbf u),\qquad
 \mathbf u_{ab}=C_D\tau^a,\quad
 \tau=-Q^{-1},\quad C_D=N^2\sin^2(3\theta)q^{3d}.
 \tag{15}
\]
The constant \(C_D\) is the original nonzero endpoint contraction.
It is not reset or suppressed in any linear identity below.

For an operator \(A_0\) on the left outer head, contraction changes
the first input seed by the anti-homomorphism
\[
 J_L(A_0)=P^{\mathsf T}A_0^{\mathsf T}(P^{\mathsf T})^{-1},
 \qquad
 J_L(K)=K^{-1},\quad J_L(E)=-K^{-1}E,\quad J_L(F)=-FK .
 \tag{16}
\]
For an operator on the right outer head the corresponding map is
\[
 J_R(A_0)=PA_0^{\mathsf T}P^{-1},\qquad
 J_R(K)=K^{-1},\quad J_R(E)=-EK^{-1},\quad J_R(F)=-KF .
 \tag{17}
\]
These follow either from (2),(12) or from the two actual cup
intertwining equations. The difference in order between (16)
and (17) is essential.
For example
\[
 J_L(FE)=EF,\qquad J_L(K^{-1}E)=-Q^{-1}E,\qquad
                              J_R(FK)=-F .
 \tag{18}
\]
All operators here act on the indicated input factor of \(A\).
They are finite matrix identities, including their top and bottom rows.

## 3. One universal Borel resolvent

On the input pair write
\[
 X=Q^{-(a+b)},\qquad Y=Q^{-b},\qquad
 Z=Q^{-a}=X/Y,\qquad R=Q^{-1}.
 \tag{19}
\]
In particular \(Z\) is not \(X^{-1}Y\).
The exact gauged \(E_A\) action from [O], divided by \(\mathbf u\), is
\[
 \mathcal L P
  =\xi R X P(RX,Y)-\xi YP(RX,Y)+(RY-1)P(RX,RY),
 \qquad K_A=RX .
 \tag{20}
\]
Substitute \(P=Y^{-1}\), as a function on the finite clock grid.
The terms proportional to \(XY^{-1}\) cancel against
\(-\xi K_A Y^{-1}\), leaving
\[
       (E_A-\xi K_A+QI)(Y^{-1}\mathbf u)
                                      =(1-\xi)\mathbf u .
 \tag{21}
\]
This calculation uses the root relation \(Y^N=1\), not an
unrecorded continuation past an endpoint.

On every even-head middle module, \(E^N=0\), \(K^N=I\), and
\(KE=QEK\). The root Gaussian-binomial identity therefore gives
\[
                  \mathcal C^N=(E-\xi K)^N
                    =(-\xi)^NI=(-1)^{N+1}I ,
 \tag{22}
\]
since \(\xi^N=-1\). Mixed Gaussian coefficients vanish because
\(Q\) is primitive and their denominator indices are less than \(N\).
This proof includes all even and composite levels.
The elementary finite geometric identity now gives
\[
 \boxed{\quad
 \mathcal R=\frac12\sum_{j=0}^{N-1}
                     (-\mathcal C)^jQ^{N-1-j}.
 \quad}                                                        \tag{23}
\]
Indeed multiplication by \(\mathcal C+Q\) gives
\(Q^N-(-\mathcal C)^N=2I\).
There is no division by a possibly vanishing channel value,
and no level \(N\) is inverted in (23).

Because \(f\) intertwines \(E,K\), it also intertwines the finite
inverse (23). Equation (21) gives
\[
 v:=f(Y^{-1}\mathbf u)=\mathcal V y,\qquad
 f(Z\mathbf u)=QK\,v .
 \tag{24}
\]
For the second identity use \(X=QK_A\), with \(K_A\) on the left.
Only the single vector \(v\) will be needed for both boundary gates.
The inverse clock modification has a different, polynomial expression:
\[
 f(Z^{-1}\mathbf u)
   =\frac{q}{q-1}K^{-1}(E-\xi K+I)y .
 \tag{25}
\]
Equation (25) concerns \(Z^{-1}=X^{-1}Y\), not \(Z\).
The latter is the clock that survives in the left Casimir below.

For the quantitative bound, the actual physical totals satisfy
\(\|E\|\le2n\), \(\|K\|=1\), hence \(\|\mathcal C\|\le2n+1\).
Formula (23) proves
\[
                  \|\mathcal R\|\le
                       \frac N2(2n+1)^{N-1}\le e^{C_nN}.
 \tag{26}
\]
This estimates the finite sum directly. It does not multiply
\(N\) unrelated inverse estimates or introduce an \(N\log N\) exponent.
Since \(|1-\xi|\le2\), it also bounds \(\mathcal V\).

## 4. Orthogonal channels for this actual resolvent

The finite Euler mechanism gives more information about the denominator.
Put \(F_r=(Q;Q)_r\), \(F_0=1\), and, on a nilpotent argument \(t^N=0\), set
\[
 \mathsf e_N(t)=\sum_{r=0}^d\frac{t^r}{F_r},\qquad
 \mathsf X=EK^{-1},\qquad
                       S=\mathsf e_N(\mathsf X/\xi)^{-1}.
 \tag{26a}
\]
The inverse polynomial is
\(\sum_{r<N}(-1)^rQ^{r(r-1)/2}t^r/F_r\).
Finite Gaussian convolution proves this inverse and
\(\mathsf e_N(Qt)=(1-t)\mathsf e_N(t)\); no \(F_N\) is used.
Also \(\mathsf X^N=0\) and \(K\mathsf XK^{-1}=Q\mathsf X\).
Consequently
\[
 SKS^{-1}=(1-\mathsf X/\xi)K,\qquad
 \mathcal C=-\xi SKS^{-1},\qquad
 \mathcal V=S(1-\xi)(Q-\xi K)^{-1}S^{-1}.
 \tag{26b}
\]
For example \(S^{-1}=\mathsf e_N(\mathsf X/\xi)\) and
\(K S^{-1}=\mathsf e_N(Q\mathsf X/\xi)K
=(1-\mathsf X/\xi)S^{-1}K\), which proves the first identity
with its displayed order.

In the positive metric
\[
 G_C=S^{-\dagger}S^{-1},
 \quad\text{the singular multipliers of }\mathcal V\text{ are }\quad
 \frac{\sin3\theta}{|\sin((2j-5)\theta)|},\qquad 0\le j<N,
 \tag{26c}
\]
with their actual physical multiplicities. Indeed \(K\) is already
unitary diagonal on the physical middle packet, with eigenvalues \(Q^j\).
The denominator \(Q-\xi Q^j\) has modulus
\(2|\sin((2j-5)\theta)|\), while \(|1-\xi|=2\sin3\theta\).
All the displayed angles are odd half-grid angles. Thus
\[
                  \|\mathcal V\|_{G_C}\le3,\qquad
                  \|\mathcal V^{-1}\|_{G_C}\le N .
 \tag{26d}
\]
For the first bound use
\(\sin3\theta\le3\sin\theta\) and the minimum denominator sine
\(\sin\theta\). For the second use
\(\sin3\theta\ge\sin\theta\ge1/N\) and the maximum denominator
sine at most one. These inequalities include \(N=2\).
In this metric \(\mathcal C\) itself is unitary. Its channels
are orthogonal physical \(K\)-weight channels in the \(S^{-1}\)
coordinates, not a value-only reduction of a pair Casimir.

This specified metric is in the controlled exponential window:
\[
             \|S^{\pm1}\|\le e^{C_nN},\qquad
             \|G_C^{\pm1}\|\le e^{C_nN},\qquad
                            \|\log G_C\|=O_n(N).
 \tag{26e}
\]
To prove the bounds, use \(\|\mathsf X\|\le2n\) and
\(|F_r|^{-1}\le2^{d-r}/N\), obtained from
\(\prod_{a=1}^d(1-Q^a)=N\) by bounding the complementary factors by two.
The finite forward and inverse Euler coefficients have the same
absolute values. Summing their \(N\) terms gives (26e) directly.

Every literal internal middle crossing, and every internal pair
Casimir, commutes with the total \(E,K\), hence with \(S\).
Those gates remain literal after this change of coordinates.
All other data must be changed as well:
\[
 \bar y=S^{-1}y,\quad
 \overline{\mathcal Y}_b=S^{-1}\mathcal Y_b,\quad
 \bar T_i=S^{-1}T_iS,\quad
 \bar y_{\rm in}=S^{-1}y_{\rm in},\quad
                         \bar\Lambda=\Lambda S .
 \tag{26f}
\]
In particular the entire outer coefficient \(C_{L,+}QK\)
is conjugated; the total \(K\) in that factor is not silently left unchanged.
The transformed input and closing are not asserted to have polynomial
norm, and the outer coefficient costs remain. The constant bound
(26d) concerns this shared resolvent in this exact metric.
The Euler/Pascal coherent-Gram mechanism is already present in [A,B];
its application to the specified denominator is the assertion here.

## 5. The left boundary, with its original endpoint coefficients

The direct expansion of the original unscaled Casimir is
\[
 \begin{split}
 \Omega_{12}={}&
 (FE)_1K_2+F_1E_2+(K^{-1}E)_1(FK)_2\\
 &+K_1^{-1}(FE)_2+qK_1K_2+q^{-1}K_1^{-1}K_2^{-1}.
 \end{split}                                                   \tag{27}
\]
After (16), every left endpoint contraction is one of the
following ratios on the first input coordinate of (15):
\[
 \begin{array}{c|c}
 \text{outer operator }A_0&
           J_L(A_0)\mathbf u\,/\,\mathbf u\\ \hline
 FE& RZ+QZ^{-1}-2\\
 F& q^3(1-Z)\\
 K^{-1}E& R^3Z-R^2\\
 K^{-1}&xZ=-q^{-1}Z\\
 K&x^{-1}Z^{-1}=-qZ^{-1}.
 \end{array}                                                   \tag{28}
\]
For instance \(J_L(F)=-FK\) gives the second row by applying
the literal first-head \(F,K\) to \(\tau^a\).
The first row is \(EF\), whose diagonal is
\(Q^{-(a+1)}+Q^{a+1}-2\).
Every missing arrow in deriving the table carries its exact
factor \(1-Q^0\) or \(1-Q^N\).

Put \(y_+=f(Z\mathbf u)\), \(y_-=f(Z^{-1}\mathbf u)\).
The observation of (27) is exactly
\[
 \begin{split}
 K_1(Ry_++Qy_--2y)
 &+q^3E_1(y-y_+)\\
 &+F_1K_1(R^3y_+-R^2y)+xF_1E_1y_+\\
 &+qx^{-1}K_1y_-+q^{-1}xK_1^{-1}y_+ .
 \end{split}                                                   \tag{29}
\]
The \(y_-\) coefficient vanishes, since \(Q+qx^{-1}=0\).
The remaining \(y\) coefficient is \(C_{L,0}\) of (8).
Before simplification the \(y_+\) coefficient is
\[
 RK_1-q^3E_1+R^3F_1K_1+xF_1E_1+q^{-1}xK_1^{-1}.
 \tag{30}
\]
Use the one-head identity following (4), together with \(x=-q^{-1}\).
This gives exactly \(C_{L,+}\) in (8).
Finally \(y_+=QK\mathcal V y\) by (24), proving the left formula
and the identity (10) at \(i=1\).
No crossing scalar \(\kappa\) belongs to this Casimir calculation.

## 6. The right boundary and literal interior gates

Using the one-head identity on both factors, the same original
pair Casimir, with middle head \(n\) on the left, can be written
\[
 \begin{split}
 \Omega_{\rm right}
  ={}&F_n\otimes E+(K_n^{-1}E_n)\otimes FK\\
    &-[2I+(q+q^{-1})K_n^{-1}]\otimes K
                                      -2K_n^{-1}\otimes I .
 \end{split}                                                   \tag{31}
\]
This is an identity of the original two-head matrices, with the
last tensor factor the right outer head.
The required right endpoint ratios, by (17), are
\[
 \begin{array}{c|c}
 \text{outer operator }A_0&
           J_R(A_0)\mathbf u\,/\,\mathbf u\\ \hline
 E&q-q^3Y^{-1}\\
 FK&Y^{-1}-1\\
 K&-qY^{-1}\\
 I&1 .
 \end{array}                                                   \tag{32}
\]
For example \(J_R(E)=-EK^{-1}\) acts on the second input
vector \(\mathbf1\), giving
\(-(Q^{-(b+1)}-1)x^{-1}Q^{b+1}=q-q^3Q^b\).
This fixes the order and phase of the first row.

The exact contraction of (31) is therefore
\[
 F_n(qy-q^3v)+K_n^{-1}E_n(v-y)
      +q[2I+(q+q^{-1})K_n^{-1}]v-2K_n^{-1}y
                 =C_{R,0}y+C_{R,+}v .
 \tag{33}
\]
Use \(v=\mathcal V y\) to obtain the right formula in (9).
It uses the same auxiliary vector as the left boundary, without
reflecting or moving the original marked row.

For \(2\le i\le b-2\), the pair is entirely inside \(W\).
It commutes with the endpoint contraction, so directly
\[
       \mathscr D\Omega_{i,i+1}\Phi
                    =\Omega^W_{i-1,i}\mathscr D\Phi .
 \tag{34}
\]
Equations (29),(33),(34) prove the complete identity (10).
The elementary head bounds \(\|E_j\|,\|F_j\|\le2\),
\(\|K_j^{\pm1}\|=1\), together with (26), prove (11)
on the whole unconstrained middle packet.

For the degenerate even width \(b=2\), no middle head remains.
Its invariant space is the original cup line, and
\(\Omega_{12}p=(q+q^{-1})p\). Thus its transported Casimir is
that scalar; the two boundary formulas with local middle
heads are only used when \(b\ge4\).

## 7. The complete braid representation and its source

Every physical pair Casimir commutes with the total small Hopf
action and the unrolled weight. It also preserves the saturated
generic source, since it is the specialization of the literal
generic pair Casimir acting on generic invariant tensors.
Thus (10), together with the faithful reconstruction of [O],
shows that the operators (9) preserve all the stated images.
In particular, on \(\mathcal K_W\),
\[
 P_N(T_i)=0,\qquad
 P_N(z)=2T_N(z/2)+2,\qquad
                    [T_i,T_j]=0\quad(|i-j|>1).
 \tag{35}
\]
Here \(T_N\) on the right is Chebyshev.
These follow by transporting the full physical identities of [P].
They have not been asserted on the entire free \(W\), nor
declared a characterization of the unrolled or saturated source.

Let \(r_N\) be exactly [M]'s original degree-\(<N\) braid
polynomial, with its prescribed values and first derivatives
at every repeated root of \(P_N\).
Let \(s_N\) be its literal inverse in \(\mathbb C[z]/P_N\).
Then the complete signed braid generators on \(\mathcal K_W\) are
\[
       \widetilde R_i^+=\kappa r_N(T_i),\qquad
       \widetilde R_i^-=\kappa^{-1}s_N(T_i),\qquad
                    \kappa=q^{d^2/2}.
 \tag{36}
\]
Their restriction to \(\mathcal Y_b\) is the actual source
representation. They satisfy the braid relations and are
inverse signed generators there because the original matrices do.
Polynomial functional calculus retains all pair-Casimir
Jordan derivatives. Replacing \(r_N\) by its nodal values
would change the actual representation.

The bounded-order rational formulas are those for the Casimirs
and their shared resolvent, not a bounded-order assertion for
the \(N\)-dependent polynomial \(r_N(T_i)\).
No new coarse bound for the physical braid norm is needed:
faithfulness gives, with the original physical norm retained,
\[
 \|\widetilde R_i^\pm|_{\mathcal Y_b}\|
                  \le e^{C_bN}\|R_i^\pm|_{\mathcal S_b}\|_{\rm ph}.
 \tag{37}
\]
This does not estimate the actual remaining word or convert
an exponential metric cost into a polynomial one.

The input and readout also remain explicit. For \(b=2k\ge4\),
the original cup packet has observation
\[
 y_{\rm in}=\mathscr D(p^{\otimes k})
       =C_D\,(\tau^a)_a\otimes p^{\otimes(k-2)}\otimes\mathbf1 .
 \tag{38}
\]
Let \(\ell_0=\ell^{\otimes(k-1)}\otimes m\) be the literal
last-mark row. Its transported row is
\[
          \Lambda(y)=\ell_0\Phi_{f_y}.
 \tag{39}
\]
For every original regular braid word, with all original
framing and external factors denoted by \(\chi_N\),
\[
 K_N=\chi_N\,\Lambda\!\left(
       \widetilde R_{i_s}^{\epsilon_s}\cdots
       \widetilde R_{i_1}^{\epsilon_1}y_{\rm in}\right).
 \tag{40}
\]
Any splitting of the original factor \(\chi_N\) must use its
original convention. It has not been bounded or divided out.
Equation (39) retains the full marked cap; it is not a
positive trace or a new favorable source row.

## 8. The original input has an explicit cost in the coherent metric

The constant resolvent bound does not make the actual source inexpensive.
Its cost can be evaluated for the original input itself. On the pair
\(A=V\otimes V\), let \(S_A\) be (26a), with the literal vector
\(\mathbf u\) of (15). Then, at every \(N\ge2\),
\[
 \boxed{\quad
 \|S_A^{-1}\mathbf u\|_{\rm ph}^2
   =|C_D|^2\sum_{\substack{k,j\ge0\\k+j\le d}}
       |(q^{-1};Q)_k|^2
                      \left|{k+j\brack k}_Q\right|^2 .
 \quad}                                                        \tag{40a}
\]
This is a positive identity for one specified actual source, not an
absolute-value replacement for a coherent contraction.

Here is a finite derivation, with the root cutoff retained.
Use the input clocks (19), put \(a_*=\xi RX\), and let
\(f_r=\mathbf u^{-1}E_A^r\mathbf u\), as in [O].
The ordered identity
\((EK^{-1})^r=Q^{r(r+1)/2}K^{-r}E^r\) and the factorial reflection
\(F_r=(-1)^rQ^{r(r+1)/2}(R;R)_r\) give
\[
 \frac{S_A^{-1}\mathbf u}{\mathbf u}
   =\sum_{r=0}^d\frac{(-1)^ra_*^{-r}f_r}{(R;R)_r},\qquad
 f_r=\sum_{k\le r}{r\brack k}_R
       L_kY^k(-1)^{r-k}(a_*;R)_{r-k}.
 \tag{40b}
\]
The second identity is exactly [O]'s finite orbit formula, with
\(L_k=\prod_{h=1}^k(R^h-\xi)\).
For \(m<N\), subtracting consecutive right sides proves
\[
 \sum_{r=0}^m\frac{(a_*;R)_ra_*^{-r}}{(R;R)_r}
         =\frac{a_*^{-m}(a_*R;R)_m}{(R;R)_m}.
 \tag{40c}
\]
Its \(m=0\) case is one, so the subtraction proves it by induction.
Apply (40c) after interchanging the finite sums in (40b).
Use
\(L_k=R^{k(k+1)/2}(\xi Q;Q)_k\),
\({d\brack k}_R=(-1)^kR^{-k(k+1)/2}\), and
\((R;R)_d=N\). All phases then give
\[
 \frac{S_A^{-1}\mathbf u}{\mathbf u}
    =\frac{a_*^{-d}}N
        \sum_{k=0}^d(q^{-1};Q)_k(a_*R;R)_{d-k}Y^k .
 \tag{40d}
\]
No factorization across terms with total index at least \(N\) was used.

The clocks \(X,Y\) are independent uniform \(N\)-point clocks and
\(|a_*|=1\). First apply Parseval in \(Y\), and then expand
\((a_*R;R)_{d-k}\) by the finite Gaussian-binomial formula and
apply Parseval in \(X\). Each sum contributes its factor \(N\),
canceling the squared prefactor \(N^{-2}\) in (40d). The result is
\(|C_D|^2\sum_{k+j\le d}|(q^{-1};Q)_k|^2
|{d-k\brack j}_R|^2\).
Factorial reflection gives the exact magnitude identity
\[
 \left|{d-k\brack j}_R\right|
   =\frac{|F_{k+j}|}{|F_k|\,|F_j|}
   =\left|{k+j\brack k}_Q\right|,
 \tag{40e}
\]
which proves (40a), including its edges.

The rate of this actual source cost is explicit. For \(1\le k<N\), put
\(R_k=\prod_{h=1}^k\sin(h\delta)/\sin((h-\tfrac12)\delta)\),
where \(\delta=\pi/N\). This product first increases and then decreases.
Its endpoints are \(R_0=1\), \(R_d=N\sin\theta\ge1\), so \(R_k\ge1\).
On the increasing half, monotonicity of \(\sin t/t\) gives
\(R_k\le\prod_{h\le k}h/(h-\tfrac12)\le2k\le N\);
for \(h\ge2\), bound the ratio by \(h/(h-1)\) to telescope.
The decreasing half has the same upper bound. Consequently
\[
 N^{-2}\le
 \frac{|(q^{-1};Q)_k|}{|F_k|}
    =\frac{\sin\theta}{R_k\sin((k-\tfrac12)\delta)}
       \le1,\qquad
 N^{-4}\sum_{0\le j\le t\le d}\left|\frac{F_t}{F_j}\right|^2
 \le\frac{\|S_A^{-1}\mathbf u\|^2}{|C_D|^2}
 \le\sum_{0\le j\le t\le d}\left|\frac{F_t}{F_j}\right|^2 .
 \tag{40f}
\]
At \(k=0\) the ratio is one, so the comparison includes that edge.

Write \(I(t)=\int_0^t\log(2\sin\pi s)\,ds\).
The uniform factorial estimate in [A] gives
\(\log|F_r|=NI(r/N)+O(\log N)\).
The maximum of \(I(t)-I(j)\), \(0\le j\le t\le1\), is achieved
at \(j=1/6,t=5/6\), with value \(v_3/\pi\).
Here
\(v_3=2\Lambda(\pi/6)=3\Lambda(\pi/3)\),
\(\Lambda(t)=-\int_0^t\log|2\sin s|\,ds\);
the equality follows from the double-angle integral identity.
The nearest grid pair gives a lower bound, while the at most
\(N^2\) terms give the upper bound. Equations (40a)--(40f) prove
\[
                  \log\|S_A^{-1}\mathbf u\|
                          =\frac{v_3}{\pi}N+O(\log N).
 \tag{40g}
\]
Thus a genuine source exponential remains in this coherent frame.

For the original width \(b=2k\), insert the interior invariant cups by
\(J(v\otimes w)=v\otimes p^{\otimes(k-2)}\otimes w\).
This is an actual \(E,K\)-intertwiner, so
\[
 S_W^{-1}y_{\rm in}=J(S_A^{-1}\mathbf u),\qquad
 \|S_W^{-1}y_{\rm in}\|^2
      =N^{3(k-2)}\|S_A^{-1}\mathbf u\|^2,\qquad
 \log\|S_W^{-1}y_{\rm in}\|
                        =\frac{v_3}{\pi}N+O_b(\log N).
 \tag{40h}
\]
Only the known polynomial cup norms were added. The closing remains
\(\Lambda S_W\). The physical row computed next does not bound this
conjugated row; no polynomial closing budget in this coherent metric,
or closed-scalar lower bound, is inferred.

## 9. The original marked closing is an explicit physical row

At four heads, the complete pair commutant [P] writes the actual
curried intertwiner as \(f=f(\Omega)\), with a unique representative
of degree at most \(d\) modulo \(P_N\).
The literal cups and last marked cap in (12)--(14) give
\[
 \lambda_4(f):=(\ell_{12}\otimes m_{34})\Phi_f
       =\frac{x^d}{N}\operatorname{Tr}(Q^{a_1}f).
 \tag{40i}
\]
Indeed their entrywise contraction is
\(x^dN^{-1}\sum_{a,c,e}Q^a f_{(a,c),(a,e)}\).
The actual pair intertwiner preserves integer degree by [P],
so only \(c=e\) remains. The indices \(a_1,a_2\) below mean
the physical occupations in these traces.

Let \(\mathsf J|a\rangle=|d-a\rangle\) and
\(\mathsf W=\mathrm{flip}(\mathsf J\otimes\mathsf J)\).
The identities \(\mathsf JE\mathsf J=-F\),
\(\mathsf JF\mathsf J=-E\), \(\mathsf JK\mathsf J=K^{-1}\)
show that \(\mathsf W\) sends the total \(E,F,K\) to
\(-F,-E,K^{-1}\). Their commutator therefore gives
\(\mathsf W\Omega\mathsf W=\Omega\).
Consequently
\(\operatorname{Tr}(Q^{a_1}f)=Q^{-1}\operatorname{Tr}(Q^{-a_2}f)\).
Since \(x^dQ^{-1}=(-1)^dx\), (40i) equals exactly [P]'s
original fixed-root functional \(\phi(f)\). In particular
\[
                         \lambda_4(f)=(-1)^dN^2[f]_d .
 \tag{40j}
\]
Here \([f]_d\) is the top coefficient of that degree-\(<N\)
representative, with every Hermite direction retained.

We compute that coefficient directly from the observed vector
\(y=f(\Omega)\mathbf u\). In the pair coideal kernel
\(B_\sigma^{12}z=\sigma z\), write \(z=\sum_a|a\rangle\otimes z_a\).
Its first row gives
\[
 z_1=\frac{B_\sigma+q^{-1}\sigma}{1-Q}z_0,\qquad
 \pi_0\Omega z=
   -q^{-1}(1-Q)FKz_1-qFEz_0-Kz_0-K^{-1}z_0 .
 \tag{40k}
\]
These identities follow from (2)--(4); the upper arrow
\(q(1-Q)\) is nonzero even at \(N=2\).
Substitution yields the actual radial operator on the remaining head,
\[
 A_\sigma=-K-K^{-1}-q^{-2}\sigma FK
                     -q^{-1}\sigma F-q^{-1}FKF .
 \tag{40l}
\]
On \(Y^r=Q^{-rb}\) it is tridiagonal in the clock powers, with
coefficients of \(Y^{r+1}\) and \(Y^{r-1}\), respectively,
\[
 a_r=(Q^r-q)(Q^r-Q^{-1}),\qquad
 c_r=Q^{-1}(Q^r-1)(Q^r-q^3),\qquad
 \prod_{r=0}^{d-1}a_r=\frac{2Nq^4}{1-q^3}=:\mathfrak h .
 \tag{40m}
\]
These follow by applying the displayed one-head matrices to \(Y^r\).
In particular \(c_0=a_d=0\), while \(a_0,\ldots,a_{d-1}\ne0\).
For the product, separate the excluded \(Q^{-1}\) factor from
\(\prod_{r=0}^d(Q^r-q)=2(-1)^{N+1}\), and differentiate
\(t^N-1\) at \(t=Q^{-1}\) for the other factor.

Since \(\pi_0\mathbf u=C_D\mathbf1\), the top clock coefficient
of \(\pi_0y=f(A_\sigma)C_D\mathbf1\) is \(C_D\mathfrak h[f]_d\).
There is no wrap before degree \(d\). Finite Fourier extraction
and (40j) therefore give the explicit row on the actual image:
\[
 \boxed{\quad
 \Lambda_4(y)=\alpha_4(y):=
       \frac{c_\Lambda}{N}\sum_{b=0}^d Q^{-b}y_{0,b},\qquad
 c_\Lambda=\frac{(-1)^dN(1-q^3)}{2C_Dq^4},\qquad
 \|\alpha_4\|_{\rm ph}=\frac1{N^{3/2}\sin3\theta}.
 \quad}                                                        \tag{40n}
\]
The norm is that of this explicit extension to the full physical pair.
It follows from \(|c_\Lambda|=1/(N\sin3\theta)\) and its \(N\)
unit-modulus coefficients. No source scalar is used to normalize it.

For width \(b=2k\ge4\), let
\(L_{\rm int}=I\otimes\ell^{\otimes(k-2)}\otimes I:W\to V\otimes V\).
It contracts exactly the original interior ordinary pairs.
Those literal caps commute with the two endpoint observations,
so the original last-mark row, with no relocation, is
\[
 \boxed{\quad
 \Lambda(y)=\alpha_4(L_{\rm int}y)\quad(y\in\mathcal Y_b),\qquad
 \|\alpha_4L_{\rm int}\|_{\rm ph}
                    =\frac{N^{-(k+1)/2}}{\sin3\theta}.
 \quad}                                                        \tag{40o}
\]
The extension norm uses \(\|\ell\|=N^{-1/2}\) on each disjoint pair.
All phases in (40n), the original last mark, and the external
\(\chi_N\) in (40) remain. After the coherent change of metric
the closing is still \((\alpha_4L_{\rm int})S_W\); its norm or
asymptotic has not been estimated here.

## 10. Linear auxiliary gate and remaining limits

The shared vector can equivalently be retained as a linear
auxiliary packet:
\[
        (E-\xi K+QI)v=(1-\xi)y,\qquad
 T_1y=C_{L,0}y+C_{L,+}QKv,\qquad
 T_{b-1}y=C_{R,0}y+C_{R,+}v .
 \tag{41}
\]
Its solution is unique on the whole \(W\), with the bound (26).
Thus these particular boundary Casimir steps have explicit
linear residual equations of bounded algebraic order. Their
squared residual energies are quadratic in the retained vectors.
The coefficients and their known exponential budgets must
still be carried in any normalized compiler.
No recompilation of a whole quartic objective is asserted here.

Although \(y\) lies in the actual constrained image, \(v\)
need not. Imposing its coideal, unrolled or divided-current
equations on that auxiliary packet would be an extra projection.
Only the final combinations in (9), on their stated domains,
are known to preserve the source. This is why all intermediate
physical coordinates are kept.

[O] already proves faithfulness, explicit reconstruction and
the exact image constraints of these observations.
[M] already gives complete all-width source modules, actual
braids and original closing rows; [P] already gives the full
pair commutant and its repeated-root Casimir algebra.
[A,B] already provide finite Euler/Pascal metrics, literal Borel
fusion and source-preserving cap transport. No first coherent
Gram, first Borel model or first quantum-group factorization is claimed.
The addition here is the explicit general-width transport of
both boundary Casimirs through these particular observations:
the two literal cup-transpose tables, the cancellation of one
endpoint clock, and the shared universal Borel inverse with
denominator two and a controlled physical norm. The actual input cost
in its coherent metric and the original physical closing row are also
computed, with their separate scope retained.

This supplies actual gate formulas, not a common positive
pairing for arbitrary signed words. The original source
constraints and coherent closing remain necessary. No
geometric trial field, cap noncancellation estimate or
finite-exception volume theorem is proved by (40)--(41).

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| O | [All-width marked-mode observation](research_all_width_marked_mode_observation.md) | 591 | b2ec8912696338d23e67e2ceb3e69a3fd5a1e20dfcfbe49228cd514a7d40f3f7 |
| M | [Complete original source multiplicities](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_source_multiplicity_module.md) | 602 | 14cfb558f50c5b091cec9439692dfeb87129e31f38588cb1ebfd8e8547ac99a9 |
| P | [Full physical pair commutant](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pair_casimir_commutant_and_rotated_trace.md) | 331 | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| A | [Earlier actual Pascal coherent Gram](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pascal_coherent_gram.md) | 494 | b6e6d697b4e21d30ca683f265b9c41170a0bee424d783169b2e0c70233dc889e |
| B | [Actual Borel fusion and divided cap period](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_borel_regular_fusion_and_divided_cap_period.md) | 361 | 1d6953e47a2aedd795982886064e03bd8ae1cbe97a3fc868c60cd4d82b9cd971 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
