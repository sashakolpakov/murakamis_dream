# An all-level local lift of the faithful beta packet

Written proof, 23 November 2026. This note defines an explicit marked
local lift of the nine-cell kernels to every integer level and evaluates
its two faithful boundary packets. After the same continuant completion,
they are exactly the original positive and negative physical crossings.
Every Casimir normal and every displayed scalar is retained.

At odd levels the local kernels are precisely the earlier charged
kernels. At even levels this is a specified local extension, with
integer charge lifts and the physical square root of the quantum
parameter. It is not attributed to an existing even-level charged
invariant. No global charged Pachner theory, tetrahedral symmetry,
positive geometric period or volume lower bound is asserted.
The earlier odd-level final [V] and all frozen files remain unchanged.

## 1. The marked data at every level

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad x=-q^{-1},\quad \gamma=-q.
 \tag{1}
\]
Thus \(\gamma^2=Q\). Define
\[
 g(j)=\gamma^{j^2}\qquad(j\in\mathbb Z).
\]
The two identities needed below hold at every level:
\[
 g(j+N)=g(j),\qquad g(j+k)=g(j)g(k)Q^{jk}.
 \tag{2}
\]
Indeed \(\gamma^{N^2}=(-1)^{N(N+1)}=1\), and
\(\gamma^{2Nj}=Q^{Nj}=1\). The second assertion is the expansion
of \((j+k)^2\). At odd \(N\),
\(\gamma=Q^{(N+1)/2}\), so \(g(j)\) is exactly the original
\(Q^{j^2/2}\), with its half taken modulo \(N\).

Choose six distinct complex decorations \(z_0,\ldots,z_5\) and
jointly marked nonzero roots
\[
                    s_{ij}^{\,N}=z_i-z_j\qquad(i<j).
 \tag{3}
\]
Work on a lifted regular domain for these roots and all normalization
square roots below. For a sorted cell \(T=abcd\), put
\[
 X_T=s_{ad}s_{bc},\quad Y_T=s_{ab}s_{cd},\quad
 Z_T=s_{ac}s_{bd},\quad
 \alpha_T=X_T/Z_T,\quad\beta_T=Y_T/Z_T.
 \tag{4}
\]
The Pluecker identity gives
\(\alpha_T^N+\beta_T^N=1\). Both parameters are nonzero. Set
\[
 W_T(n)=\prod_{j=1}^{[n]}\frac{\beta_T}{1-\alpha_TQ^j},\qquad
 \overline W_T(n)=\prod_{j=0}^{[n]-1}
                         \frac{\beta_T}{1-\alpha_TQ^j}.
 \tag{5}
\]
Here \([n]\in\{0,\ldots,d\}\), and empty products are one.
Every denominator is nonzero. The product around a whole period is
\(\beta_T^N/(1-\alpha_T^N)=1\), so both functions extend
periodically to all integers. The bar is a label, not conjugation.

The normalization is fixed before any boundary coefficient is evaluated.
For a cell write
\[
 (P,Q_0,R,B,C,H)=(s_{ab},s_{bc},s_{cd},s_{ac},s_{bd},s_{ad}),
\]
and use the literal finite normalizations of [B]:
\[
 \langle U,V\rangle=\frac{U^N-V^N}{N(U-V)},\qquad
 k_*=\frac{\langle B,Q_0\rangle^{1/2}\langle H,R\rangle^{1/2}
                         \langle C,R\rangle^{1/2}}
                        {\langle H,C\rangle^{1/2}},
\]
\[
 v(u;r)=\prod_{j=1}^r(1-uQ^j)^{-1},\qquad
 f(u,v\mid z)=\sum_{r=0}^{d}\frac{v(u;r)}{v(v;r)}z^r,
 \qquad z^N=\frac{1-u^N}{1-v^N},
\]
\[
 u=R/H,\quad v=R/(QC),\quad z=BC/(HQ_0),\qquad
 \rho_T=k_*f(u,v\mid z),\quad
 \bar\rho_T=k_*f(Qv,u/Q\mid z^{-1}).
 \tag{6}
\]
The same marked root \(k_*\) is used twice. No normalization is chosen
from a physical crossing or its source value.

These factors are units at every level. The finite product proof in
[B, Section 2] uses only cyclic sequences and Fourier sums, and gives
\[
 f(u,v\mid z)f(Qv,u/Q\mid z^{-1})
 =\frac{N(1-Qv)(1-u)(1-z^N)(Qvz-u)}
 {(1-u^N)(1-z)(Qv-u)},
\]
\[
                  \rho_T\bar\rho_T
                     =\frac{(PR)^N}{N(BC-HQ_0)}\ne0.
 \tag{7}
\]
For clarity, no parity premise enters that proof: after regrouping its
two finite sums by the index difference, every nonzero difference gives
a polynomial in \(Q^r\) of degree \(N-2\), with constant term one;
Fourier summation retains only that term. The zero difference is the
elementary sum \(\sum_r(1-tQ^r)^{-1}=N/(1-t^N)\).
Substitution of the displayed roots proves (7). Their central
differences and partial sums are nonzero by (3), so the literal
denominators are units. This is the same finite normalization calculation
as [B], without its charged odd-level interpretation.

## 2. The local charge lift and the nine kernels

Choose integer marks \(h_1,\ldots,h_4\) with
\(\sum_mh_m=2\). Use either sector
\((r_1,r_2,r_3,r_4)=(1,0,0,0)\) or \((0,0,0,1)\).
The following is the complete lifted charge table; temporarily it also
makes sense for any integer sector with \(\sum r_m=1\):
\[
\begin{array}{c|ccc}
T&a&b&c\\\hline
1234&0&1/2&0\\
1245&0&1/2&0\\
2345&1&-1/2&0\\
0123&-r_2&r_1+r_2-1/2&1-r_1\\
0134&1-r_3&1/2-r_4&-r_1-r_2\\
0125&r_2+r_3-h_1&h_1+r_4-1/2&r_1\\
0235&1+r_3-h_1-h_2&h_1+h_2-r_2-r_3-1/2&r_2\\
0345&h_4-1&3/2-h_4-r_3&r_3\\
0145&0&1/2-r_4&r_4
\end{array}.
 \tag{8}
\]
Thus \(a,c\) are integers and \(b=1/2-a-c\) is a marked
half-integer. These are the same exact affine charge equations as [S],
now read in \(\tfrac12\mathbb Z\), rather than using an inverse of
two modulo an even integer. Every tetrahedral vertex sum is \(1/2\).
The non-link interior edge totals are one and the two link totals are
zero. For example the latter are
\(1/2+(r_1+r_2-1/2)-r_1-r_2=0\) and
\(1/2+0-1/2=0\). The boundary totals are \(h_m,1-h_m\),
and the four distinct \(05\) totals are \(r_m\).

Face indices \(\alpha,\beta,\eta,\delta\) lie in \(\mathbb Z/N\).
Define the two local kernels explicitly by
\[
 T_T(a,c)_{\alpha,\beta}^{\eta,\delta}
 =\rho_T Q^{c(\eta-\alpha)+\alpha\delta}
       \gamma^{ac+\alpha^2}W_T(\eta-a-\alpha)
                                      \delta_{\beta,\eta+\delta},
\]
\[
 \bar T_T(a,c)_{\eta,\delta}^{\alpha,\beta}
 =\bar\rho_T Q^{c(\eta-\alpha)-\alpha\delta}
       \gamma^{-ac-\alpha^2}\overline W_T(\eta+a-\alpha)^{-1}
                                      \delta_{\beta,\eta+\delta}.
 \tag{9}
\]
These are well-defined cyclic face tensors by (2),(5). Their charge
marks are not silently reduced modulo \(N\) at even levels:
\(a\mapsto a+N\), for example, can change \(\gamma^{ac}\) by
\((-1)^c\). Marks modulo \(2N\) suffice. At odd levels (9)
coincides with [S, (3)] and its specified scalar normalization.
At even levels (9) is the new local definition used in this note.

Use the nine signs
\[
\begin{array}{c|rrrrrrrrr}
T&1234&1245&2345&0123&0134&0125&0235&0345&0145\\\hline
\text{sign}&+&+&+&+&+&-&-&-&+
\end{array}
 \tag{10}
\]
and the original face slots
\((\alpha,\beta,\eta,\delta)=(\alpha_3,\alpha_1,\alpha_2,\alpha_0)\).
Here is the complete internal pairing, with omitted local vertices
in parentheses:
\[
\begin{array}{c|ll}
123&1234(3)&0123(0)\\
124&1234(2)&1245(3)\\
134&1234(1)&0134(0)\\
234&1234(0)&2345(3)\\
013&0123(2)&0134(3)\\
245&1245(0)&2345(1)\\
012&0123(3)&0125(3)\\
125&1245(2)&0125(0)\\
023&0123(1)&0235(3)\\
235&2345(2)&0235(0)\\
034&0134(1)&0345(3)\\
345&2345(0)&0345(0)\\
014&0134(2)&0145(3)\\
145&1245(1)&0145(0)
\end{array}.
 \tag{11}
\]
The boundary faces are, respectively,
\((015,025)=(p_1,m_2)\) for \(0125\),
\((025,035)=(p_2,m_3)\) for \(0235\),
\((035,045)=(p_3,m_4)\) for \(0345\), and
\((015,045)=(m_1,p_4)\) for \(0145\).
Multiply the contraction by its original edge factor
\[
                 \mathfrak e=(s_{12}s_{23}s_{34}s_{14})^{-d}.
 \tag{12}
\]
Call the resulting boundary arrays \(B_+^{\rm lift}\) and
\(B_-^{\rm lift}\) in the two sectors. This defines them directly
from local kernels, not from a desired crossing row.

## 3. The six sums and their phases at all levels

Put \(k_m=[m_m-p_m+h_m]\). Name the fourteen internal indices as
in [S]: \(A,B,C,D,E,F,G,H,I,J,K,L,M,V\) on the fourteen faces
in the order displayed in (11). The deltas give
\[
 C=B+D,\quad V=H+F,\quad F=J+L,\quad I=E+A,\quad K=M+C,
\]
\[
 H=m_2-p_1,\quad J=m_3-p_2,\quad L=m_4-p_3,\quad V=p_4-m_1.
 \tag{13}
\]
Their compatibility is precisely \(\sum k_m=2\) modulo \(N\).
No eliminated sum contributes a factor \(N\). On this support use
\[
 u=B-A,\quad v=H-B,\quad \tau=J-1-D,\quad
 r=E-G,\quad s=M-1-E,\quad z=m_1-M.
 \tag{14}
\]
The inverse is
\(B=H-v,A=H-v-u,D=J-1-\tau,M=m_1-z,\)
\(E=m_1-1-z-s,G=m_1-1-z-s-r\).
It is an affine bijection over every \(\mathbb Z/N\).

For the canonical sector the signed sum of the constant \(ac\)
terms is \(h_1-1\). The integer non-Gaussian exponent before (14) is
\[
 AD+BF+DL+GA+EC-IJ-KL+MV-GH-M+E+p_1-G.
\]
The Gaussian ratio is exactly
\[
 \frac{g(A)g(B)g(D)g(E)g(M)}{g(I)g(K)}
                         =Q^{-EA-MB-MD-BD}.
 \tag{15}
\]
Indeed use (13), periodicity of \(g\), and its polarization in (2).
Thus no representative-dependent quadratic carry is dropped. Substitution
of (14) in the remaining integer exponent gives \(\Xi+h_1\), where
\[
 \Xi=u(1+\tau+r)+v(1+r+s)+(1+\tau)(1+s)+z+r-k_1.
\]
Writing
\[
 \mathfrak n=\mathfrak e\,
 \rho_{1234}\rho_{1245}\rho_{2345}\rho_{0123}\rho_{0134}
 \bar\rho_{0125}\bar\rho_{0235}\bar\rho_{0345}\rho_{0145},
 \tag{16}
\]
the canonical array is therefore zero off its support, and on it equals
\[
\begin{split}
 B_0^{\rm lift}(\mathbf k)=\mathfrak n\gamma^{3h_1-1}
 \sum_{u,v,\tau,r,s,z} Q^{\Xi}
 \frac{W_{1234}(u)W_{1245}(v)W_{2345}(\tau)
       W_{0123}(r)W_{0134}(s)W_{0145}(z)}
 {\overline W_{0125}(1-k_1+r+s+z)
  \overline W_{0235}(2-k_1-k_2+u+v+s+z)
  \overline W_{0345}(k_4+\tau+v+z)}.
\end{split}
 \tag{17}
\]
All six indices are cyclic. Equation (17) is obtained from the nine
defined kernels, not independently assigned.

For the negative sector no change in the six arguments is needed.
The changed linear charge phases contribute \(Q^{k_1-h_1}\);
the changed \(ac\) terms contribute \(\gamma^{1-h_1}\).
Consequently
\[
 B_+^{\rm lift}=B_0^{\rm lift},\qquad
 B_-^{\rm lift}(\mathbf k)
                 =Q^{k_1}\gamma^{1-3h_1}B_0^{\rm lift}(\mathbf k).
 \tag{18}
\]
This also follows by putting the two integer sectors into (8),(9).
The phase agrees with [S, (17b)] at odd levels and is fixed by
the displayed lift at even levels.

The calculation shows that each array depends on its eight boundary
indices only through \(\mathbf k\). A prescribed \(\mathbf k\)
has \(N^4\) paired-face lifts. Its paired average is therefore
\(N^{-4}\) times their sum, and equals the displayed coefficient.

## 4. The scalar beta identity and the retained quotient

For five increasing labels define, with the fixed finite \(f\) of (6),
\[
 \mathfrak f_{abcde}
  =f(\alpha_{abcd},\alpha_{abce}/Q
                         \mid\beta_{abcd}/\beta_{abce}).
 \tag{19}
\]
At every level its exact scalar convolution is
\[
 \sum_r Q^{Kr}\frac{W_{abcd}(r)}{\overline W_{abce}(r+L)}
 =\mathfrak f_{abcde}
 \frac{\overline W_{acde}(K+L)}
      {\overline W_{bcde}(K)\overline W_{abde}(L)}.
 \tag{20}
\]
Here is a parity-independent verification. If \(a_r\) is the cyclic
summand of \(f(x,y\mid z)\), its recurrence is
\((1-xQ^{r+1})a_{r+1}=z(1-yQ^{r+1})a_r\). Summation gives
\[
 (1-z)f(x,y\mid z)=(x-Qyz)f(x,y\mid Qz),
\]
\[
 f(x,Qy\mid z)
     =\frac{x-Qy}{(1-Qy)(x-Qyz)}f(x,y\mid z).
 \tag{21}
\]
Use \(x=\alpha_{abcd},y=\alpha_{abce}/Q\),
\(z=\beta_{abcd}/\beta_{abce}=\alpha_{bcde}\).
The two sides of (20) have the same \(K,L\) steps by (21) and
the monomial identities
\[
 \alpha_{acde}=\alpha_{abce}z/x,\quad
 \alpha_{abde}=\alpha_{abce}/x,\quad
 \beta_{acde}/\beta_{bcde}=1/x,\quad
 \beta_{acde}/\beta_{abde}=1/\beta_{abce}.
\]
At \(K=L=0\) they agree by (19). Every step multiplier is a unit
on the regular domain, so this proves (20) around the whole cyclic seam.
If \(\mathfrak f\) vanished, all \(K\) values at \(L=0\)
would vanish. Fourier inversion would then annihilate the nonzero
summand vector. Thus these finite normalizers are units too.

Apply (20) first to the \(r\)-sum in (17), with
\(K=u+v+1,L=1-k_1+s+z\). The distinguished retained quotient is
\[
 \frac{\overline W_{0235}(K+L)}
      {\overline W_{0235}(K+L-k_2)}.
 \tag{22}
\]
It is identically one at \(k_2=0\), before any remaining sum.
Deleting only (22) thus leaves both faithful slices below unchanged.
All other factors and phases in (17),(20) remain. This is an exact
local beta elimination for the defined lifted kernels, not a global
even-level charged Pachner assertion.

## 5. Complete evaluation on the two faithful slices

Stay on the support \(\sum_mk_m=2\) modulo \(N\), and impose
\(k_2=0\). Set
\[
 a=[-k_1],\qquad C=[k_3-1]+1\in\{1,\ldots,N\},
 \qquad b=[-C].
 \tag{23}
\]
Write \((z;Q)_n=\prod_{j=0}^{n-1}(1-zQ^j)\) and
\({n\brack r}_Q=(Q;Q)_n/[(Q;Q)_r(Q;Q)_{n-r}]\) for
\(0\le r\le n<N\), and set the latter to zero otherwise.
All factorial denominators here are nonzero.
Use the following exact scalar, without changing any normalization:
\[
\begin{split}
 J={}&\mathfrak n\,
 \mathfrak f_{01235}\mathfrak f_{01345}\mathfrak f_{12345}N^3
 \frac{1-\alpha_{1245}}{\beta_{1245}}
 \frac{1-\alpha_{2345}}{\beta_{2345}}
 \frac{1-\alpha_{0145}}{\beta_{0145}}
 \frac{\beta_{1345}}{1-\alpha_{1345}^{N}} .
\end{split}
 \tag{24}
\]
This is exactly [E, (4)]. In particular it retains all nine cell
normalizers, all three beta sums, the three factors \(N\), and the
displayed linear factors. It is a unit by (4),(7),(20).

After the first beta sum, sum \(s\) using \(01345\), with
\(K=v+\tau+1,L=z+1-k_1\), then \(u\) using \(12345\),
with \(K=\tau+1,L=v+1\). Direct substitution of (20) and
\(W(z)/\overline W(z+1)=(1-\alpha)/\beta\) leaves the following
three sums. Put \(K_*=J(1-\alpha_{1345}^N)/N^3\); then
\[
\begin{split}
 B_0^{\rm lift}(\mathbf k)
 ={}&K_*\gamma^{3h_1-1}Q^{1-k_1}
          \beta_{0145}^{-a}\beta_{0345}^{-b}
 \sum_{v,\tau,z}\frac{Q^{v+\tau+z}}
                   {1-\alpha_{1345}Q^{v+\tau+1}}\\
 &\quad\cdot\prod_{j=1}^{a}(1-\alpha_{0145}Q^{z+j})
       \prod_{j=0}^{b-1}
          (1-\alpha_{0345}Q^{v+\tau+z+2-k_1+j}).
\end{split}
 \tag{25}
\]
This records the precise remaining factors. In particular (25) does
not estimate the beta kernels by their absolute values.

For \(0\le h\le b\) expand the second product by the finite
binomial theorem. Its coefficient is
\((-\alpha_{0345})^hQ^{h(h-1)/2}{b\brack h}_Q\).
The exact \(v\)-sum is
\[
 \sum_v\frac{Q^{(1+h)v}}
                 {1-\alpha_{1345}Q^{v+\tau+1}}
 =\frac{N\alpha_{1345}^{d-h}}{1-\alpha_{1345}^N}
                  Q^{-(1+h)(\tau+1)}.
 \tag{26}
\]
It follows by multiplying by \(1-\alpha_{1345}^N\), expanding
the finite geometric numerator, and taking the one surviving Fourier
coefficient. The remaining \(\tau\) exponent is zero, so its sum
is \(N\). In the first product of (25), let the degree be \(e\).
The \(z\)-sum selects \(1+h+e=N\), hence \(e=d-h\), and
contributes the third \(N\). There is no other possible multiple:
\(1\le1+h+e\le2N-1\).

Use \(\alpha_{1345}\alpha_{0145}=\alpha_{0345}\).
The two product signs have total \((-1)^d\); their quadratic
exponent is
\[
 \frac{h(h-1)}2+\frac{(d-h)(d-h+1)}2
                  =\frac{Nd}{2}-Nh+h^2.
\]
All these are ordinary integers. Since
\((-1)^dQ^{Nd/2}=1\) at every level, the result is
\[
\begin{split}
 B_0^{\rm lift}(\mathbf k)
 ={}&J\gamma^{3h_1-1}Q^{-k_1}
       \beta_{0145}^{-a}\beta_{0345}^{-b}\alpha_{0345}^{d}
                         S(a,b;k_1),\\
 S(a,b;k_1)
 ={}&\sum_{h=0}^b {b\brack h}_Q{a\brack d-h}_Q
                                  Q^{h^2+h(1-k_1)}.
\end{split}
 \tag{27}
\]
Invalid binomial coefficients are zero. Every factorial index is below
\(N\). Equations (25)--(27) are a direct finite calculation with
all endpoints and normalizations retained.

For the positive faithful row take
\[
 \mathbf k_+(j)=(1,0,[j+1],[-j]),\qquad 0\le j\le d.
 \tag{28}
\]
Then \(a=d,C=j+1\). Reflection of the numerator factors gives
\({d\brack h}_Q=(-1)^hQ^{-h(h+1)/2}\). Thus
\[
 S(d,b;1)=\sum_{h=0}^b{b\brack h}_Q
                  (-1)^hQ^{h(h-1)/2}=(1;Q)_b.
\]
It is zero for \(j<d\), when \(b=N-j-1\ge1\), and one for
\(j=d\), when \(b=0\). Therefore
\[
 B_+^{\rm lift}(\mathbf k_+(j))
   =J\gamma^{3h_1-1}Q^{-1}
           (\alpha_{0345}/\beta_{0145})^d\delta_{j,d}.
 \tag{29}
\]

For the negative faithful column take
\[
 \mathbf k_-(i)=([-i],0,1,[i+1]),\qquad 0\le i\le d.
 \tag{30}
\]
Here \(a=i,C=1,b=d\), and \(1-k_1\equiv1+a\).
Insert the same reflection formula for \({d\brack h}_Q\) in
(27), then put \(e=d-h\). The result, including its constant, is
\[
 S(a,d;k_1)=Q^{-a}(Q^{1-a};Q)_a=\delta_{a,0}.
 \tag{31}
\]
For example the constant before the binomial sum is
\((-1)^dQ^{d(d+1)/2+ad}=Q^{-a}\), and the remaining argument
is \(Q^{1-a}\). If \(a\ge1\), its finite product contains
\(1-Q^0\). If \(a=0\), it is the empty product.
Multiplying by the original negative sector phase (18) gives
\[
 B_-^{\rm lift}(\mathbf k_-(i))
                 =J(\alpha_{0345}/\beta_{0345})^d\delta_{i,0}.
 \tag{32}
\]

There is a useful check against the rational-coefficient calculation
in [E, (20)]. At the surviving endpoints its rational function is
\((1-X)^{-1}\). Both coefficients \([X^d]\) and \([X^{2N-1}]\)
equal one. Their displayed combination is
\((1-\alpha_{0345}^N)^{-1}\), not one. At both endpoints the
rational formula's prefactor satisfies
\(\beta_{0345}^{C}=\beta_{0345}^{-b}\beta_{0345}^{N}\).
Its factor \(\beta_{0345}^N=1-\alpha_{0345}^N\) cancels the
displayed denominator and leaves \(\beta_{0345}^{-b}\). Thus the
rational rewrite retains its high coefficient even in this slice.
The direct calculation (25)--(27) avoids deleting or estimating that
carry. No assertion of its vanishing is used.

## 6. The specified port pullback and original signed crossings

Define, from the already fixed finite quantities,
\[
 C_N=\frac{J}{N^2}
 \left(\frac{s_{34}}
 {s_{01}s_{02}s_{03}s_{35}s_{45}^{\,2}}\right)^d,
 \qquad f_m(k)=s_{0m}^{[k-1]}s_{m5}^{[-k]}.
 \tag{33}
\]
This is the same explicit expression as [E, (4)]. It is a unit,
with its phase and every marked root retained. No even-level
real-decoration modulus assertion is needed.

Use the following explicit selected port scalars:
\[
 e^+_j=C_N\gamma^{3(h_1-1)}s_{05}^dN^2Qx^{-j}
                         \prod_{m=1}^4f_m(k_{+,m}(j)),
\]
\[
 e^-_i=C_Ns_{05}^dN^2x^{i-d}
                         \prod_{m=1}^4f_m(k_{-,m}(i)).
 \tag{34}
\]
They are defined nonzero local pullback factors at every level.
At odd levels they are exactly the original selected port scalars
of [R,V]. We do not assume the odd-level all-boundary port theorem
as a theorem for even levels. Instead the selected comparisons follow
directly from (29),(32).

At the positive surviving tuple \((1,0,0,1)\), the products in (33)
give
\[
 C_NN^2s_{05}^d\prod_m f_m(k_m)
                  =J(\alpha_{0345}/\beta_{0145})^d.
\]
At the negative surviving tuple \((0,0,1,1)\), they give
\[
 C_NN^2s_{05}^d\prod_m f_m(k_m)
                  =J(\alpha_{0345}/\beta_{0345})^d.
 \tag{35}
\]
For the first use
\(\alpha_{0345}/\beta_{0145}
 =s_{05}s_{34}s_{15}/(s_{35}s_{01}s_{45})\);
for the second use
\(\alpha_{0345}/\beta_{0345}=s_{05}s_{34}/(s_{03}s_{45})\).
Since \(\gamma^2=Q\), \(x^2=Q^{-1}\), and
\(Qx^{-2d}=1\), equations (29),(32)--(35) prove
\[
 w_j:=(e^+_j)^{-1}B_+^{\rm lift}(\mathbf k_+(j))
                             =x^{-d}\delta_{j,d},
\]
\[
 v_i:=(e^-_i)^{-1}B_-^{\rm lift}(\mathbf k_-(i))
                             =x^d\delta_{i,0}.
 \tag{36}
\]
Explicitly the positive surviving phase ratio is
\(\gamma^2Q^{-2}x^d=Q^{-1}x^d=x^{-d}\), and the negative
one is \(x^d\). None is fixed afterward by comparison with a
desired source value.

By [H], at every \(N\ge2\) the actual full signed crossings satisfy
\[
 e_0^{\mathsf T}R_+|_{W_d}
       =\kappa x^{-d}e_d^{\mathsf T},\qquad
 R_-|_{W_d}e_d=\kappa^{-1}x^de_0,
 \qquad \kappa=q^{d^2/2}.
 \tag{37}
\]
The first is the literal sparse checked-crossing row in [H, Section 3].
The second follows by inversion and symmetry of complete pair boxes.
Consequently (36) gives exactly the entire first row of the stripped
positive crossing and the entire last column of the stripped negative
crossing, including their zero entries. It does not assert that the
other entries of a raw pulled-back array agree with a physical crossing.

The same result holds after deleting (22), since both observed
tuples have \(k_2=0\). If \(w^\flat,v^\flat\) denote the
ratio-free selected data, then \(w^\flat=w,v^\flat=v\).
One can take their paired averages before (34); the averaging factor
is exactly \(N^{-4}\), as established after (18).

## 7. Full-normal completion and source scope

For completeness the reconstruction is purely finite algebra.
Let \(A=\Omega|_{W_d}\) be the actual complex symmetric irreducible
tridiagonal Casimir, with diagonal \(a_j\) and nonzero offdiagonal
\(b_j=-(1-Q^{j+1})^2\). Its full minimal polynomial is
\(P_N=2T_N(z/2)+2\). Put
\[
 p_0=1,\quad p_1=z-a_0,\quad
 p_{j+1}=(z-a_j)p_j-b_{j-1}^2p_{j-1},\qquad
 B_j=\prod_{h<j}b_h,\quad u_j=p_j/B_j.
\]
Then \(u_j(A)e_0=e_j\), by induction, and symmetry gives
\(e_0^{\mathsf T}u_j(A)=e_j^{\mathsf T}\).
Thus \(I_+(w)=\sum_jw_ju_j\) is the unique polynomial class
having first row \(w\). Reversing the diagonal and offdiagonal lists
gives \(\widehat u_j(A)e_d=e_{d-j}\) and
\(I_-(v)=\sum_iv_i\widehat u_{d-i}\).
The full-pair commutant theorem identifies the resulting polynomial
class with its original operator on all physical degrees.

It follows from (36),(37), at every level, that
\[
 \boxed{\quad
 R_+=\kappa I_+(w^\flat)(\Omega),\qquad
 R_-=\kappa^{-1}I_-(v^\flat)(\Omega).
 \quad}
 \tag{38}
\]
Faithfulness uses the full minimal polynomial, including multiplicities.
In particular every first Casimir normal at a double node is retained.
These are fixed-root statements, not quantum-parameter or moving-meridian
derivative assertions.

Reconstruct before multiplying boxes, applying a genuine turn or using
the original marked closing. Then every leaf is the same complete
physical crossing by (38), and induction through any fixed literal
Conway compiler gives the same open packets and original closed scalar.
Fixed signed integer powers are included by finite multiplication.
All Cartan, pivot, framing and peripheral lines keep their original
positions. The reconstruction and inverse port factors move to an
exterior by their full bilinear dual if that representation is used.
They are not omitted on individual modified noncommutant tensors.

Likewise, replacing a leaf by its completed expression (38) leaves
the same compiler's leaf element, normalized local maps, original
budgets and degree-four objective pointwise unchanged. No old budget
is assigned to a new optimization over the uncompleted local variables.
The actual signed data have Euclidean norm one and reconstruct packets
of Newton norm \(\sqrt N\), as in [V]. This is only their particular
norm ratio, not a bound for arbitrary inverse data or for the uniform
physical Hilbert--Schmidt norm.

This proves a local all-level extension of the faithful-slice adapter.
At even levels its source is the explicitly defined marked lift (8)--(12),
and its equality to the original source is proved after the faithful
pullback and completion. It is not a claim that this raw lifted tensor
already defines a literature charged state on arbitrary triangulations.
No full even-level all-boundary crossing identification, global spin
state sum, charged Pachner invariance, geometric cycle selection,
positive closing or volume lower bound follows.

## Complete inputs and coverage

The following complete matching texts were read. Their finite formulas
fix the source data; the parity-independent lift and both selected
calculations are written out above.

| Text | Lines | SHA-256 |
|---|---:|---|
| [S: Literal nine-cell source](research_nine_tetrahedron_boundary_source_reduction.md) | 666 | 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c |
| [B: Literal finite normalizers](research_literal_charged_tetrahedron_bubble.md) | 383 | 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b |
| [E: Canonical beta evaluation](research_nine_cell_canonical_crossing_evaluation.md) | 424 | 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9 |
| [H: Actual full Casimir packets](actual_complete_casimir_hermite_packet.md) | 321 | a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c |
| [P: Full pair commutant](actual_pair_casimir_commutant_and_rotated_trace.md) | 331 | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| [V: Adopted odd-level faithful adapter](research_faithful_boundary_beta_adapter_v2.md) | 510 | fd19f126280ca6a6e307c15fe167ea787821f8f8f8e00b33404fe503d7770188 |
| [C: Original normalized compiler](research_convex_normalized_conway_source.md) | 329 | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |
| [R: Odd-level full-Psi port source](research_full_psi_ray_crossings_and_nine_cell_boundary.md) | 588 | 495a2fde1ed1d7ca0707f060208121bddb2673be21ff3bcb9bac737420ac2d24 |

The odd-level limitation of the cited charged sources is not erased.
For primary coverage, [Baseilhac--Benedetti's matrix-dilogarithm
definition](https://arxiv.org/abs/math/0306283) is indexed by odd levels.
[Ishibashi, Remark 2.2 and Appendix B](https://link.springer.com/article/10.1007/s00220-026-05604-6)
discusses the physical square-root convention at arbitrary levels with
additional signs; its [phase correction](https://arxiv.org/abs/2610.23572)
retains further root-lifting data. These are coverage statements only.
No external pentagon proof, normalization theorem or even-level state
identification is imported.

General cyclic products, quadratic refinements, finite Fourier sums,
binomial identities and continuant reconstruction are existing methods.
The source-specific assertion here is their complete signed faithful-slice
calibration for the displayed local lift. Only written mathematics and
text/hash operations were used. No mathematical program, numerical test,
build, git operation or edit to an earlier final was performed.
