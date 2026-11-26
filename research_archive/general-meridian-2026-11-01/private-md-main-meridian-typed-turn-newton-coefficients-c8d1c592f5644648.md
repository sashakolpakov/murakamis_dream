# Moving Newton coefficients of the physical quarter-turn

Private continuation, 1 November 2026. No repository file is changed.

This report derives coefficients of the physical currying operation in the Newton coordinates of the six-type compiler. The turn between opposite-color endomorphism spaces is a scalar reversal. For the remaining orientation types, an exact cup-slide and a sparse source-Casimir recurrence give a sine-binomial coefficient formula. These formulas prove polynomial coefficient norms and inverse norms before the first ordinary-color resonance. They do not by themselves compare the exponentially conditioned Newton and spectral norms.

## 1. Coordinates and the operation being computed

Put
\[
N\ge2,\quad d=N-1,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad
Q=q^2,\quad \rho=q-q^{-1},\quad M=q^s,\quad
x=-q^{-1}M,\quad y=-q^{-1}M^{-1}.
\]
The displacement lies in a fixed disk \(|s|\le R<1\). Write
\[
[a]=\frac{\sin(a\theta)}{\sin\theta},\qquad
S_n=\prod_{r=1}^n2\sin(r\theta),\qquad
P_n(s)=\prod_{r=1}^n\frac{\sin((r-s)\theta)}{\sin(r\theta)}.
\tag{1}
\]
Empty products equal one. The nilpotent modules and their duality are those of [the exact compiler](/Users/sasha/volume-conjecture/notes/actual_main_meridian_newton_compiler.md):
\[
Kv_a=xQ^{-a}v_a,\quad Fv_a=v_{a+1},\quad
Ev_a=e_a(x)v_{a-1},\quad e_a(x)=[a][a-s],
\]
\[
J_xw_a=c_a(x)\varphi_{d-a},\qquad
c_a(x)=(-x)^aQ^{a(a+1)/2}.
\tag{2}
\]
For \(V_y\), replace \(s\) by \(-s\).

On \(V_x\otimes V_x\), the nodes are
\[
c_j(s)=2\cos((2j+1-2s)\theta),\qquad
e_n^s(z)=S_n^{-2}\prod_{j=0}^{n-1}(c_j(s)-z).
\tag{3}
\]
On an opposite-color pair the nodes are \(c_j(0)\), and the Newton basis is denoted \(e_n^0\).

For an endomorphism of \(V_x\otimes V_x\), the physical turn is
\[
\mathcal T_x(A)^{jb}_{ak}
=\frac{c_a(x)}{c_b(x)}A^{d-a,j}_{k,d-b}.
\tag{4}
\]
It maps \(V_y\otimes V_x\) to \(V_x\otimes V_y\). For an endomorphism of \(V_x\otimes V_y\), the corresponding formula is
\[
\mathcal U_{x,y}(A)^{jb}_{ak}
=\frac{c_a(x)}{c_b(y)}A^{d-a,j}_{k,d-b},
\tag{5}
\]
an endomorphism of \(V_y\otimes V_x\). Both formulas follow by inserting the actual evaluation and coevaluation maps, with the two indicated dualities. Their physical entries are regular.

For (4), retain exactly the normalized carrier in the compiler:
\[
G_{-+}=\check R_{x,y}\,r_0^{-1}(\Omega_{x,y}),
\qquad G_{+-}=I.
\tag{6}
\]
Here \(r_0\) is the full complete crossing polynomial, including its Cartan scalar and confluent coefficients. We represent the output on the reference object \(V_x\otimes V_y\). Thus the polynomial to expand is
\[
\widehat{\mathcal T}_s(A)
=\mathcal T_x(A)G_{-+}
=\mathcal T_x(A)\check R_{x,y}r_0^{-1}(\Omega_{x,y}).
\tag{7}
\]
The order in (7) is essential. This is a polynomial endomorphism of the reference object; it is conjugate to the compiler's polynomial endomorphism of the input object, so its polynomial coefficients are the same. Write
\[
\widehat{\mathcal T}_s(e_n^s)=\sum_{k=0}^d T_{kn}(s)e_k^0.
\tag{8}
\]
For (5), both source and target are endomorphism objects and no mixed carrier is inserted.

## 2. Physical boundary entries recover Newton coefficients

Let \(W_t\) be the degree-\(t\) subspace, with ordered basis \(v_a\otimes v_{t-a}\), \(0\le a\le t\), for \(0\le t\le d\). Its Casimir characteristic and minimal polynomial are
\[
\prod_{j=0}^t(z-c_j).
\tag{9}
\]
The characteristic identity follows by the generic highest-vector triangular decomposition, continued as a polynomial identity to the opposite-color locus. The tridiagonal matrix is cyclic: all offdiagonal factors involved have indices between \(1\) and \(d\), and the only color factors are \([r-s]\) or \([r+s]\). None vanishes for \(|s|<1\). Thus (9) retains repeated roots and their normals.

Consequently \(e_k(\Omega)\) vanishes on \(W_t\) if \(k>t\). If \(k<t\), its first-color bandwidth is at most \(k\), so its \((0,t;t,0)\) entry vanishes. The sole surviving basis entry is
\[
\left(e_t^0(\Omega_{x,y})\right)_{(0,t);(t,0)}
=M^{-2t}P_t(s).
\tag{10}
\]
Indeed the unique path lowering the first color from \(t\) to zero has product
\[
\rho^{2t}(y/x)^t\prod_{a=1}^t e_a(x);
\]
the powers of \(Q\) sum to zero. Multiplication by the leading coefficient \((-1)^t/S_t^2\) gives (10). Thus every opposite-color polynomial \(f=\sum f_ke_k^0\) satisfies the exact extractor
\[
f_t=\frac{f(\Omega_{x,y})_{(0,t);(t,0)}}{M^{-2t}P_t(s)}.
\tag{11}
\]
This formula has no divided eigenvalue differences and is valid at all constant Casimir collisions.

Both turns (4) and (5) preserve integer degree. If their input is \(e_n(\Omega)\), their output vanishes on every \(W_t\) with \(t<d-n\): the source entry in (4) or (5) changes its first index by \(d-t>n\), outside the input bandwidth. The carrier in (6) also preserves degree. Applying (9) gives
\[
T_{kn}(s)=0\qquad(k+n<d).
\tag{12}
\]
This is an anti-triangular support statement. It does not discard the entries \(k+n>d\).

## 3. A proved scalar reversal for opposite-color endomorphisms

**Proposition.** The turn (5) is exactly
\[
\boxed{\quad
\mathcal U_{x,y}(e_n^0(\Omega_{x,y}))
=\frac{P_n(-s)}{P_{d-n}(-s)}
       e_{d-n}^0(\Omega_{y,x}).
\quad}
\tag{13}
\]

The bandwidth argument proves divisibility by \(e_{d-n}^0\). For the reverse degree bound, inspect the first row on the middle block \(W_d\). Its column \(a\) is proportional to the source diagonal entry on \(W_{d-a}\):
\[
\left(\mathcal U_{x,y}(e_n^0)\right)_{(0,d);(a,d-a)}
=\frac{c_a(x)}{c_d(y)}
   \left(e_n^0(\Omega_{x,y})\right)_{(d-a,0);(d-a,0)}.
\]
It vanishes for \(a>d-n\), by (9). The first row of the target tridiagonal Casimir is cyclic. A polynomial of degree \(r<N\) has a nonzero entry in column \(r\) from its unique outermost path. Therefore the output degree is at most \(d-n\), proving scalar reversal.

Put \(t=d-n\). In (5), the extreme entry \((0,t;t,0)\) has source indices \((n,0;0,n)\). Its unique increasing path gives \(P_n(-s)\); the duality ratio contributes \(M^{2t}\). The target \(e_t^0(\Omega_{y,x})\) has extreme entry \(M^{2t}P_t(-s)\), by (10) with \(x,y\) interchanged. Their ratio proves (13).

The other opposite-color turn replaces \(s\) by \(-s\). The reflection identity
\[
P_n(s)P_{d-n}(-s)=P_d(s)
=\frac{\sin(\pi s)}{N\sin(\pi s/N)}
\tag{14}
\]
also shows that the reversal scalar in (13) is even in \(s\), and that the two successive reversal scalars multiply to one.

These two orientation types therefore have a proved polynomial coefficient norm and inverse norm on every fixed disk \(|s|\le R<1\), by the estimates in Section 6. This is a Newton-coordinate assertion, not a Hilbert--Schmidt substitution.

## 4. An exact finite recurrence for the remaining turn coefficients

The following formulas compute every entry in (8) without spectral projectors. They are proved directly from physical matrices.

For \(0\le D\le d\), let \(O_D=\Omega_{x,x}|W_D\), and denote its entries by
\[
\begin{aligned}
(O_D)_{a,a}
&=\rho^2\left(e_a(x)xQ^{-(D-a)}
             +x^{-1}Q^a e_{D-a}(x)\right)
  +qx^2Q^{-D}+q^{-1}x^{-2}Q^D,\\
(O_D)_{a+1,a}&=\rho^2e_{D-a}(x),\\
(O_D)_{a-1,a}&=\rho^2e_a(x)Q^{2a-D-1}.
\end{aligned}
\tag{15}
\]
Outside entries are zero. Define the row
\[
E_{D,n}(j)=\bigl(e_n^s(O_D)\bigr)_{D,j}.
\]
It is computed by
\[
\begin{aligned}
E_{D,0}(j)&=\mathbf1_{j=D},\\
4\sin^2((n+1)\theta)E_{D,n+1}(j)
&=(c_n(s)-(O_D)_{j,j})E_{D,n}(j)\\
&\quad -(O_D)_{j-1,j}E_{D,n}(j-1)
       -(O_D)_{j+1,j}E_{D,n}(j+1).
\end{aligned}
\tag{16}
\]
It is zero for \(n>D\).

The full mixed braiding has Cartan scalar
\[
\kappa_{xy}=q^{(d^2-s^2)/2},\qquad \kappa_0=q^{d^2/2}.
\]
The original finite Euler expression gives
\[
\begin{aligned}
\mathcal R_{t,l}(s)
&:=\left(\check R_{x,y}\right)_{(l,t-l);(t,0)}\\
&=\kappa_{xy}x^{-l}y^{-(t-l)}Q^{(t-l)l}
  \frac{q^{l(l-1)/2}\rho^l}{[l]!}
       \prod_{r=0}^{l-1}e_{t-r}(x).
\end{aligned}
\tag{17}
\]
Indeed its uncheck nilpotent factor lowers the first color by \(l\), raises the second by \(l\), and its Cartan factor is evaluated after that transfer. Checking exchanges the two resulting colors.

Let \(H_{tn}\) be the Newton coefficient of
\(\mathcal T_x(e_n^s)\check R_{x,y}\). Equations (4), (11), and (17) give
\[
H_{tn}
=\frac{M^{2t}}{P_t(s)}
 \sum_{l=0}^{\min(t,d-n)}
   \frac{c_l(x)}{c_t(x)}
   E_{d-l,n}(t-l)\mathcal R_{t,l}(s).
\tag{18}
\]
The upper limit uses the actual vanishing \(e_n|W_{d-l}=0\) for \(l>d-n\).

Finally multiplication by the complete \(r_0^{-1}\), in the constant opposite-color algebra, has the already proved matrix
\[
C^-_{kt}
=\kappa_0^{-1}(-1)^kq^{-k(t+1)}
        \frac{S_k}{S_tS_{k-t}}\qquad(0\le t\le k).
\]
Therefore the full normalized answer is
\[
\boxed{\quad T_{kn}(s)=\sum_{t=0}^k C^-_{kt}H_{tn}(s).\quad}
\tag{19}
\]
Equations (15)--(19) are an exact finite coefficient formula with a tridiagonal recurrence. They retain every high-output entry and every complete nilpotent direction. Applying absolute values to their separate summands does not presently give a polynomial norm estimate.

## 5. Two evaluated parts of the same-color turn

The anti-diagonal of (19) has the exact value
\[
\boxed{\quad T_{d-n,n}(s)
=q^{-s^2/2}\frac{P_n(s)}{P_{d-n}(s)}.\quad}
\tag{20}
\]

Here are details fixing the carrier scalar. On the first nonzero degree \(t=d-n\), both the raw turn and \(e_t^0\) have rank one. Normalize the highest vector of \(V_x\otimes V_y\) to have coefficient one at \(v_0\otimes v_t\). The mixed braiding maps it to the analogously normalized highest vector for \(V_y\otimes V_x\), with scalar
\[
\gamma_t(s)
=\kappa_{xy}(-1)^tq^{t(t+1)}M^{2t}
       \frac{P_t(-s)}{P_t(s)}.
\tag{21}
\]
This follows from the highest-vector recurrence: its coefficient at \(v_t\otimes v_0\) is
\((-1)^ty^{-t}Q^{t(t-1)/2}\prod_{r=1}^t e_r(y)/e_r(x)\).
Only the zero-transfer term of the checked braiding reaches the first component. Dividing (21) by \(r_0(c_t)=\kappa_0(-1)^tq^{t(t+1)}\) gives the carrier scalar. The raw turn's extreme entry is \(P_n(s)\); the corresponding domain Newton entry is \(M^{2t}P_t(-s)\). Their ratio with this carrier scalar proves (20).

The full last column is also evaluated:
\[
\boxed{\quad
T_{k,d}(s)=q^{-s^2/2}P_d(s)(-q)^{-k}
                 \frac{(Y;p)_k}{(Yp;p)_k},
\quad Y=M^2,\quad p=Q^{-1}.
\quad}
\tag{22}
\]
The ratio is one at \(k=0\), and \((1-Y)/(1-Yp^k)\) for \(k>0\).

For this proof, only \(l=0\) remains in (18), since \(n=d\). The boundary row of \(e_d^s(O_d)\) is
\[
E_{d,d}(t)=P_d(s)(-x^{-1})^tQ^{t(t-1)/2}.
\]
Its first component is the unique \(d\)-step path. The remaining components follow from the left highest-vector equation
\(\ell_{t+1}=-x^{-1}Q^t\ell_t\), since \(e_d\) annihilates the descendants of the other highest vectors. Thus
\[
H_{t,d}=\kappa_{xy}P_d(s)\frac{(-qM)^t}{P_t(s)}.
\]
Substitution in (19) reduces (22) to the finite identity
\[
\sum_{t=0}^k {k\brack t}_p(-1)^tp^{t(t-1)/2}
          \frac{Y^t(p;p)_t}{(Yp;p)_t}
=\frac{(Y;p)_k}{(Yp;p)_k}.
\tag{23}
\]
Here is a direct telescoping proof. For \(k>0\), rewrite the summand as
\[
A_t=\frac{(p^{-k};p)_t}{(Yp;p)_t}(Yp^k)^t,\qquad
\frac{A_{t+1}}{A_t}
=\frac{Y(p^k-p^t)}{1-Yp^{t+1}}.
\]
Set \(A_{k+1}=0\) and \(v_t=(1-Yp^t)/(1-Yp^k)\). The displayed ratio gives
\[
v_tA_t-v_{t+1}A_{t+1}=A_t.
\]
Summing from \(0\) to \(k\) leaves \(v_0A_0=(1-Y)/(1-Yp^k)\), which is the right side of (23). The case \(k=0\) equals one directly. All denominators are nonzero on the stated disk, and clearing denominators extends the finite identity wherever defined. No infinite summation formula is needed.

## 6. Physical source identification and the full turn formula

The general identity in (24) below is now proved by an explicit three-strand source calculation. This section supplies the physical identification; the ensuing norm estimates use its coefficient factorization.

Consider intertwiners
\[
V_x\longrightarrow V_x\otimes V_x\otimes V_y.
\]
Every such intertwiner is determined by a vector \(w\) in the middle degree \(W_d\) of the first two factors. Its highest vector is
\[
H_L(w)=\sum_{c=0}^d
 \frac{(-y)^cQ^{-c(c-1)/2}}{\prod_{r=1}^c e_r(y)}
       E_{12}^c w\otimes w_c.
\tag{S1}
\]
Indeed the highest-vector equation gives
\(z_{c+1}=-yQ^{-c}E_{12}z_c/e_{c+1}(y)\).
Its last equation is \(E_{12}^Nw=0\). The total highest root is
\(x^2yQ^{-d}=x\), so the full \(F\)-string defines an intertwiner \(I_w\) from \(V_x\). All coefficients \(e_r(x)\), \(1\le r<N\), are nonzero on \(|s|<1\); the usual commutator verifies that string, and extraction at third color zero gives the inverse. Thus this is the full \(N\)-dimensional source space, not a selected eigenline.

Use the fixed complete balanced basis on \(W_d\). Its diagonal gauge from the nilpotent basis is \(\delta_j\delta_{d-j}\), with \(\delta_a=\rho^a/(Q;Q)_a\); this gauge is kept fixed while \(s\) varies. Let \(A_s\) and \(B_s\) be the actual actions of \(\Omega_{12}\) and \(\Omega_{23}\) on the source coordinate \(w\). Put \(D_s=\operatorname{diag}P_j(s)\), and write \(A_0,B_0\) for their complete values. Then
\[
B_s=D_s^{-1}B_0D_s,\qquad
(B_0)_{jj}=c_j(0),\qquad (B_0)_{j-1,j}=\rho^2[j]^2.
\tag{S2}
\]
To see this directly, only third colors zero and one in (S1) can contribute after applying \(\Omega_{23}\) and returning to third color zero. Their \(F_2E_2\) terms cancel. The remaining term is
\(-\rho^2yF_2E_1K_2\), together with the diagonal \(qK_2K_3+q^{-1}K_2^{-1}K_3^{-1}\). In the fixed balanced basis it gives diagonal \(c_j(0)\) and superdiagonal \(\rho^2[j][j-s]\), which is (S2).

The equal-color matrix has entries
\[
\begin{aligned}
(A_s)_{jj}&=(A_0)_{jj}+\rho^2[s]^2qQ^j,\\
(A_s)_{j-1,j}&=-\rho^2Q^j[j][j-s],\\
(A_s)_{j,j-1}&=-\rho^2Q^j[j][j+s].
\end{aligned}
\tag{S3}
\]
These follow by inserting the two module matrices into the coproduct Casimir. In particular,
\[
D_sA_sD_s^{-1}=A_0+\rho^2[s]^2 K,\qquad
K_{jj}=qQ^j,\quad K_{j,j-1}=Q^j.
\tag{S4}
\]
The identity \([j-s][j+s]=[j]^2-[s]^2\) gives its offdiagonal entries.

Let \(R_0=r_0(B_0)\), and let \(J\) reverse the \(N\) coordinates. The full complete crossing matrix is
\[
(R_0)_{ij}
=\kappa_0(-1)^jq^{j+i^2}{j\brack i}_Q
\qquad(i\le j).
\tag{S5}
\]
The existing complete-source identity is
\(R_0^{-1}A_0R_0=B_0^T\).
It is the full physical Gaussian conjugation from [the canonical source graph](/Users/sasha/volume-conjecture/notes/actual_newton_twist_canonical_graph.md), including repeated channels.

The new perturbation conjugates just as explicitly:
\[
R_0^{-1}KR_0=-S_{\mathrm{lower}}
                   +(-1)^N e_0e_d^T,
\tag{S6}
\]
where \(S_{\mathrm{lower}}e_j=e_{j+1}\) for \(j<d\), and its last column is zero. For \(j<d\), the \(i\)-th entry of \(KR_0e_j\), after removing the common scalar
\(\kappa_0(-1)^jq^{j+i^2+1}\), is
\[
Q^i{j\brack i}_Q+{j\brack i-1}_Q
={j+1\brack i}_Q.
\]
Hence that column is \(-R_0e_{j+1}\). In the last column, the same identity gives \({N\brack i}_Q=0\) for \(1\le i<N\), while its zeroth entry is \((-1)^N\kappa_0\). Since \(R_0e_0=\kappa_0e_0\), (S6) follows.

Define
\[
S_s=J R_0^{-1}D_s.
\]
Equations (S2), (S4), and (S6) give
\[
S_sB_sS_s^{-1}=Z_0,\qquad
S_sA_sS_s^{-1}=L_s,
\tag{S7}
\]
where \(Z_0=B_0^T\), and the only nonzero entries of \(L_s\) are
\[
\begin{aligned}
(L_s)_{kk}&=c_k(0),\\
(L_s)_{k-1,k}&=-4\sin((k-s)\theta)\sin((k+s)\theta)
                        &&(1\le k\le d),\\
(L_s)_{d,0}&=(-1)^{N+1}4\sin^2(s\theta).
\end{aligned}
\tag{S8}
\]
The wrap entry is retained.

It remains to identify this source coordinate change with the actual turn, rather than merely a matrix with the desired spectrum. The required cup-slide is exact. Apply (S1) to \(w=e_d\). Only \(E_1K_2\) acts, and
\(e_{N-r}(x)=e_r(y)\), so
\[
H_L(e_d)=\sum_{c=0}^d
 (-1)^cQ^{-c(c+1)/2}
 v_{d-c}\otimes v_0\otimes w_c.
\tag{S9}
\]
The positive mixed braiding on the last two factors has only its zero-transfer term here. It gives
\[
\check R_{23}H_L(e_d)
=\kappa_{xy}\sum_{c=0}^d c_c(x)^{-1}
          v_{d-c}\otimes w_c\otimes v_0
=\kappa_{xy}\operatorname{coev}_{x,y}\otimes v_0.
\]
Both sides are intertwiners, so equality on the generating highest vector proves
\[
\check R_{23} I_{e_d}
=\kappa_{xy}(\operatorname{coev}_{x,y}\otimes I_x).
\tag{S10}
\]
The fixed balanced gauge multiplies both source endpoints \(e_0,e_d\) by the same constant, and leaves this scalar unchanged.

For any equal-color polynomial \(f(\Omega_{x,x})\), the actual currying and snake equations now imply
\[
\bigl[\mathcal T_x(f)\check R_{x,y}\bigr]_{23} I_{e_d}
=\kappa_{xy}I_{\,f(A_s)e_0}.
\tag{S11}
\]
In coordinates, its left side is \(h(B_s)e_d\), where
\(h=\widehat{\mathcal T}_s(f)\,r_0\).
The opposite-color Newton basis satisfies
\(e_k^0(B_s)e_d=P_k(-s)e_{d-k}\).
Combining this with (14) and \(r_0(B_s)=D_s^{-1}R_0D_s\), one obtains the exact coefficient-vector formula
\[
\boxed{\quad
\operatorname{coeff}\widehat{\mathcal T}_s(f)
=\frac{\kappa_{xy}}{P_d(s)}
            S_s f(A_s)e_0.
\quad}
\tag{S12}
\]
This identifies every input coefficient with the original physical turn, carrier, and duality.

Consequently \(T_sZ_s=L_sT_s\), where input multiplication \(Z_s\) has diagonal \(c_n(s)\) and subdiagonal \(-4\sin^2((n+1)\theta)\). The initial column is
\(T_se_0=(q^{-s^2/2}/P_d(s))e_d\).
These data determine all columns successively by
\[
T_se_{n+1}
=\frac{c_n(s)I-L_s}{4\sin^2((n+1)\theta)}T_se_n
\qquad(0\le n<d).
\tag{S13}
\]

The sine-binomial expression (24) satisfies exactly this recurrence. For \(m=k+n-d\ge0\), the required interior scalar identity is
\[
\sin((n+1)\theta)\sin((n+1-s)\theta)
 -\sin((k+1)\theta)\sin((k+1+s)\theta)
=-\sin((m+1)\theta)\sin((n-k-s)\theta).
\tag{S14}
\]
It follows by product-to-sum and \(n+k+2=N+m+1\). Together with
\(b_{m+1}/b_m=[s-m]/[m+1]\) and
\(P_{n+1}/P_n=[n+1-s]/[n+1]\), it gives the interior recurrence. One can clear those factors before checking the identity, so their zeros cause no restriction. If \(m<-1\), all terms are zero; the boundary \(m=-1\) is the same identity before cancellation. At \(k=d\), the recurrence reduces to
\[
c_n(s)-c_d(0)
=4\sin((n+1-s)\theta)\sin((s-n)\theta),
\]
which is again product-to-sum. The wrap term does not act on the first \(d\) input columns because their zeroth coordinate is zero. It remains present in the full intertwining equation (S7), including the last column. The initial column agrees with (20), so induction proves (24) for every index.


## 7. The closed formula and polynomial coefficient bounds

The physical source calculation in Section 6 proves the complete coefficient identity
\[
\boxed{\quad
T_{kn}(s)=
q^{-s^2/2}\frac{P_n(s)}{P_k(s)}
       b_{k+n-d}(s),\qquad
b_m(s)=\prod_{r=0}^{m-1}
          \frac{\sin((s-r)\theta)}{\sin((r+1)\theta)}.
\quad}
\tag{24}
\]
Here \(b_0=1\) and \(b_m=0\) for negative integers \(m\). All complete repeated-root directions are retained.

For its coefficient norm, Let \(D_s=\operatorname{diag}P_n(s)\), let \(J\) reverse indices, and let \(B_s\) be lower triangular Toeplitz with entry \(b_{k-t}(s)\). The exact matrix is
\[
q^{-s^2/2}D_s^{-1}B_sJD_s.
\tag{25}
\]
The exact finite convolution identity is
\[
B_sB_{-s}=I.
\tag{26}
\]
For example, before specializing \(Q\), write
\[
b_m(s)=(-q^{s+1})^m
       \frac{(Q^{-s};Q)_m}{(Q;Q)_m}.
\]
The formal binomial series has generating function
\[
\sum_{m\ge0}b_m(s)z^m
=\frac{(-q^{1-s}z;Q)_\infty}
       {(-q^{1+s}z;Q)_\infty}.
\]
This formal identity follows by comparing the constant term and the first-order \(Q\)-difference equation, whose coefficient recurrence is the displayed ratio for \(b_m\). Multiplying the series for \(s,-s\) gives one. Only coefficients of degree below \(N\) are used, so their denominators remain nonzero at the root. This proves (26) by specialization of finite identities.

Both \(D_s\) and \(D_s^{-1}\) have polynomial operator norms for \(|s|\le R<1\). For the upper bound, compare each shifted sine factor with its unshifted factor and sum \(1/\min(r,N-r)\). For the lower bound, with \(d_r=\min(r,N-r)\),
\[
|\sin((r-s)\theta)|\ge
\sin((r-\operatorname{Re}s)\theta)
\ge (1-R/d_r)\sin(r\theta).
\]
The first inequality uses the modulus formula for sine; the second follows from concavity of sine between the nearest endpoint and \(r\theta\). Hence
\[
|P_n(s)|+|P_n(s)|^{-1}\le C_RN^{A_R}
\tag{27}
\]
uniformly in \(n,N\). Negative real sine signs do not occur here because \(1\le r<N\) and \(|\operatorname{Re}s|<1\).

For \(m\ge1\), there is the exact simplification
\[
b_m(s)=(-1)^{m-1}
       \frac{\sin(s\theta)}{\sin(m\theta)}P_{m-1}(s).
\tag{28}
\]
Equations (27)--(28) and the harmonic sum give polynomial bounds on the row and column sums of \(B_s,B_{-s}\). Thus the matrix in (25), and its inverse, have uniform polynomial coefficient norms. Every fixed \(s\)-derivative has the same kind of bound on a smaller disk, by Cauchy's formula.

These estimates establish polynomial control for the specified same-color-to-mixed turn and its linear inverse. Two further identifications give the actual forward turns in the other orientation types.

First, two successive physical currying operations give the dual endomorphism. Explicitly, their composition on \(A\in\operatorname{End}(V_x\otimes V_x)\) has entries
\[
\frac{c_a(x)c_k(x)}{c_b(x)c_j(x)}
 A^{d-k,d-a}_{d-b,d-j}.
\tag{29}
\]
This is the ordinary dual matrix under the reversed tensor-order identification by \(J_x\). The Casimir is fixed by the antipode:
\[
\rho^2EF+qK^{-1}+q^{-1}K
=\rho^2FE+qK+q^{-1}K^{-1}.
\]
Therefore \(f(\Omega_{x,x})\) becomes the same polynomial \(f(\Omega_{y,y})\). Its selected Newton frame changes from \(e^s\) to \(e^{-s}\). The second forward turn is consequently
\[
C_{s\to -s}\,T_s^{-1},
\tag{30}
\]
where \(C_{s\to -s}\) is the coefficient connection in column convention. It is polynomially bounded with its inverse by the two complete-frame connections already proved in the compiler. Any double-dual pivotal conjugation is trivial on the Casimir centralizer.

Second, replacing \(s\) by \(-s\) in (24) swaps the reference order of the opposite-color object. This requires a scalar carrier correction, which can be computed with all confluent coefficients retained. Temporarily use generic highest weights
\[
\alpha=d+s+\varepsilon/2,\qquad
\beta=d-s+\varepsilon/2.
\]
On the channel indexed by \(j\), the full two-color monodromy has eigenvalue
\[
q^{\alpha\beta-2j(\alpha+\beta)+2j(j-1)}.
\tag{31}
\]
For example, multiply the two highest-vector braid scalars in (21) before imposing the opposite-color condition; their factorial ratios cancel. Replacing \(\alpha,\beta\) by the equal pair \(d+\varepsilon/2,d+\varepsilon/2\) keeps every Casimir node unchanged and changes the exponent in (31) by precisely \(-s^2\). Thus the two generic polynomial monodromies differ by \(q^{-s^2}\). Continuing \(\varepsilon\) to zero gives the full Hermite identity
\[
\check R_{y,x}\check R_{x,y}
=q^{-s^2}r_0(\Omega)^2.
\tag{32}
\]
This continuation retains the divided differences at every paired node; equivalently, it is a regular physical matrix identity, and the moment pairing uniquely determines its polynomial at \(|s|<1\).

Let \(G'=\check R_{y,x}r_0^{-1}\) be the reference carrier obtained by replacing \(s\) by \(-s\). Equation (32) says \(G'G_{-+}=q^{-s^2}I\). For a turn \(\mathcal B:V_x\otimes V_y\to V_y\otimes V_x\), the fixed-reference polynomial is \(G_{-+}^{-1}\mathcal B\), while its natural sign-reversed presentation is \(\mathcal B G'\). Conjugating by \(G_{-+}\) shows that their coefficient vectors differ by the scalar \(q^{s^2}\). This scalar and its inverse are bounded on a fixed \(s\)-disk. Thus the actual sign-reversed forward turn is covered as well. Applying (30) to it covers the fourth type in that orbit.

Together with the two opposite-color endomorphism turns (13), this proves polynomial coefficient norms and inverse norms for all six orientation types. It does not give a uniform weighted norm for an arbitrary exponentially varying diagonal weight; that would require checking its ratios against this nontrivial triangular support.

## 8. The first derivative in fixed polynomial coordinates

There is an additional consistency with the connection derivative in the moving multiplication calculation. Cotangent reflection gives
\[
P_n'(0)=P_{d-n}'(0),
\]
and \(q^{-s^2/2}\) has zero first derivative at zero. For \(m>0\),
\[
b_m'(0)=(-1)^{m+1}
              \frac{\pi}{N\sin(\pi m/N)}.
\tag{33}
\]
If \(D\) is the strictly lower triangular Toeplitz matrix with those entries, the moving-Newton turn therefore satisfies
\[
T_0'=DJ.
\tag{34}
\]
Define the connection \(C_s\) by \(e_n^s=\sum_k(C_s)_{nk}e_k^0\). The same \(D\) is precisely \(C_0'\). In column coefficient convention, returning the input to the fixed complete polynomial basis gives \(T_sC_s^{-T}\). Its derivative is \(DJ-JD^T=0\), since \(D\) is Toeplitz. Consequently the normalized physical turn in fixed polynomial coordinates has zero first derivative at completeness. The nonzero derivative (34) is entirely the moving-basis contribution. This first-order statement does not erase the nonzero higher-order deformation or its high-output entries.

## 9. Scope of the coefficient estimate

The cup-slide (S10) and the original snake identity identify (24) with the actual physical turn. The coefficient estimate therefore controls all six orientation types, with inverse maps, on every fixed disk before the first ordinary-color resonance. It does not automatically give a polynomial bound in the full spectral-jet or Chebyshev norm, since the complete Newton-to-spectral change of basis itself can have exponential condition number.

Even polynomial control of all typed turns would not erase the new same-color multiplication sectors. Those are present in the already proved moving multiplication table. A whole-knot estimate must contract those actual gates with the physical closing functional and any signed half-twist sums. No conclusion here identifies the regular microscopic profile with one or changes the original volume theorem.

