# A whole-interval upper rate for turned microscopic endpoint products

Private written proof, 16 November 2026.

The exact divided-difference product module, including its polynomial
channel gauge and forced recovery, gives a regular finite physical
recurrence. Its full value/normal transfer has the terminal maximal
characteristic rate. The original fixed-row initialization can itself
have that rate. Keeping both costs gives a uniform upper bound of twice
the terminal integral for every fixed ordinary endpoint product.

This is an upper bound, not a nonzero coefficient or a filled-action
comparison. The conclusion for one unit turn is subexponential
stability of the whole product. It does not say that its image is
another endpoint product, or that arbitrary repeated tree elimination
stays in this class.

## 1. Original source and statement

Use the original normalizations
\[
 q=e^{\pi i/N},\quad D=N-1,\quad \eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\quad c_j=2\cos((2j+1)\pi/N),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 e_j(Z)=S_j^{-2}\prod_{a<j}(c_a-Z),
\]
\[
 S_j=\prod_{a=1}^j2\sin(a\pi/N),\quad
 Te_j=e_{D-j},\quad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\quad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
 \tag{1}
\]
The symbol \(T_N\) denotes Chebyshev's polynomial; \(T\) is the
original physical turn, and \(R\) the original crossing. Put
\[
 C f=Zf\pmod {P_N},\quad J=TCT,\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n},
\]
\[
 Q_0(Z)=\partial_wK_N(c_0,Z),\qquad
 G_n=T(R^{-n}),\qquad H_n=T(R^{-n}Q_0).
 \tag{2}
\]
All canonical real norms below are on the ordinary interval
\([-2,2]\). Parameters \(w_i\) remain ordinary variables before
their indicated substitution; no exterior quotient is imposed.

For fixed \(n\ne0\), let \(\tau_{\ell,n}(u)\), \(1\le\ell\le|n|\),
be the distinct physical terminal shift roots on \(0<u<1/2\).
Each retains its algebraic multiplicity two. Define
\[
 L_n(u)=\max_\ell\log|\tau_{\ell,n}(u)|,\qquad
 \mathcal I_n=\int_0^{1/2}L_n(u)\,du,\qquad \mathcal I_0=0.
 \tag{3}
\]
The whole-terminal source proves that this improper integral is
finite, \(L_n\ge0\), and \(L_1=L_{-1}=0\).

**Theorem 1.** Fix integers \(r\ge1,n\), and a finite \(A\).
For \(|\alpha_i|\le A\), set
\[
 w_i=2\cosh(\alpha_i/N),\qquad
 B_{\boldsymbol\alpha,N}
      =\operatorname{can}\prod_{i=1}^rK_N(w_i,Z).
 \tag{4}
\]
Then
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N
  \log\left(1+\sup_{|\alpha_i|\le A}
       \|V_nB_{\boldsymbol\alpha,N}\|_{\mathbb R}\right)
                       \le2\mathcal I_n .
 \quad}                                                   \tag{5}
\]
The same bound holds after any fixed number of spectral \(Z\)
derivatives and parameter \(\alpha_i\) derivatives. In particular
all original physical first normals are retained.
For \(n=\pm1\), (5) is an actual subexponential bound on the
whole turned product. No polynomial bound is asserted.

A useful quantitative version for \(n\ne0\) is the following.
For every sufficiently small fixed \(\epsilon>0\), there are
constants, uniform over (4), such that
\[
 \begin{split}
 1+\|V_nB_{\boldsymbol\alpha,N}\|_{\mathbb R}
 \le{}& C_{\epsilon}N^{p_\epsilon}
       (1+\|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R})\\
 &{}\times\exp\left\{
     N\int_\epsilon^{1/2-\epsilon}L_n(u)\,du
       +C_{n,r,A}N\epsilon\log(e/\epsilon)
       +C_\epsilon N^{1-1/(66r)}\right\}.
 \end{split}                                             \tag{6}
\]
The constant multiplying the endpoint loss is independent of
\(\epsilon\). The other constants can depend on the fixed
interior interval. This separation specifies the order of limits.

## 2. Polynomial inputs and the actual fixed-row initialization

The two-half-plane source proves that every fixed ordinary
product in (4) has polynomial real norm, uniformly on bounded
complex parameter sets, including both parities. Its proof
also supplies the single-kernel bound on any larger fixed
parameter polydisk. It uses the actual physical row/root
bound and retains the full high complement.

The six ordinary channels of the product module are
\[
 (f_i,\mathcal D f_i,\mathcal S f_i,
                 \mathcal S\mathcal D f_i,P_N,1),
 \qquad f_i=K_N(w_i,Z).
 \tag{7}
\]
Here the half-shift mean and divided difference have the exact
definitions in the module source. On the real interval their
two arguments are \(2\cos(\theta\pm\pi/N)\), both in \([-2,2]\).
The fundamental theorem of calculus on the interval between
these arguments, with its removable coincident-point limit,
gives
\[
 \|\mathcal S f\|_{\mathbb R}\le\|f\|_{\mathbb R},\qquad
 \|\mathcal D f\|_{\mathbb R}\le\|f'\|_{\mathbb R}.
 \tag{8}
\]
Markov's inequality thus bounds all channels (7) polynomially.
The same is true for their fixed tensor products and their
polynomial gauges \((Z-2)^a\), \(0\le a\le2r\).
Their ordinary degrees are \(O_r(N)\). Canonical reduction
preserves their physical values and first normals; Markov
and the stable full-Hermite reconstruction therefore keep
their canonical real norms polynomial. All these estimates
are uniform for bounded complex \(\boldsymbol\alpha\).

We need actual turned initial data for these channels. They
are not assumed polynomial after turning.

**Lemma 2.** Fix \(M,n\). If \(p_N\) is any canonical polynomial,
then, for all \(0\le j\le M\),
\[
 |(V_np_N)(c_j)|+|(V_np_N)'(c_j)|
 \le C_{M,n}N^{b_{M,n}}\|p_N\|_{\mathbb R}
          (\|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R}).
 \tag{9}
\]
For a polynomially bounded family of inputs, these data have
upper exponential rate at most \(\mathcal I_n\).

*Proof.* Write
\[
 F_j(Z)=K_N(c_j,Z),\qquad
 Q_j(Z)=\partial_wK_N(c_j,Z).
 \tag{10}
\]
The exact physical first-variable recurrence and its index
derivative, as recorded in the whole-terminal source, imply
in the full algebra
\[
 F_j=F_j(C)1,\qquad
 Q_j=a_{j,N}(C)Q_0+b_{j,N}(C)1.                          \tag{11}
\]
In (11), the first \(F_j\) on the right is its ordinary
degree-\(j\) row polynomial. The polynomials \(a_{j,N},b_{j,N}\)
have degrees bounded in terms of \(j\) alone, and coefficients
bounded by a fixed power of \(N\).

Here is the recurrence justification of this slightly stronger
form of the fixed-row estimate. Put
\[
 s_t=2\sin(t\pi/N),\quad
 A(t)=\frac{s_{t+1}^4}{s_{2t+1}s_{2t+2}},\quad
 B(t)=\frac{s_t^4}{s_{2t}s_{2t+1}}.
 \tag{12}
\]
Starting with \(F_0=1\), the value equation is
\[
 F_{j+1}=\left(1+\frac{B(j)}{A(j)}
                       +\frac{c_0-C}{A(j)}\right)F_j
                       -\frac{B(j)}{A(j)}F_{j-1}.
 \tag{13}
\]
The previous row is absent at \(j=0\).
Differentiate the original ordinary index equation, with
unknown \(c'(j)Q_j\), where \(c(t)=2\cos((2t+1)\pi/N)\).
It has the same homogeneous part, terms involving coefficient
derivatives and \(F_j,F_{j-1}\), and a scalar multiple of
\(P_N(C)\). The last term is zero in the full algebra.
The removable identities \(B(0)=B'(0)=0\) leave no
previous normal at the first row. Starting from \(Q_0\)
therefore gives (11) by induction. Every inverse sine and
every \(1/c'(j)\) involved at these fixed rows is polynomial
in \(N\); the degrees and coefficient assertions follow.
For large \(N\), all these fixed rows are double nodes.

Since \(T\) is self-adjoint for the original Frobenius pairing,
\(TC=JT\), and multiplication by \(R^{-n}\) commutes with \(C\),
\[
 T(R^{-n}F_j)=F_j(J)G_n,\qquad
 T(R^{-n}Q_j)=a_{j,N}(J)H_n+b_{j,N}(J)G_n.               \tag{14}
\]
The original kernel evaluation gives exactly
\[
 \begin{split}
 (V_np_N)(c_j)
     &=\kappa^n\phi_N\big(F_j(J)G_n\,p_N\big),\\
 (V_np_N)'(c_j)
     &=\kappa^n\phi_N\big(
             [a_{j,N}(J)H_n+b_{j,N}(J)G_n]p_N\big).
 \end{split}                                             \tag{15}
\]
Every product and its product-rule normal is inside this
trace. In particular the normal term is \(H_n\), not
\(V_nQ_0\).

The operator source proves \(\|J\|_{\mathbb R}\le34N^3\).
For canonical \(f,p\), Markov followed by full-Hermite
reconstruction and the trace norm gives
\[
             |\phi_N(fp)|\le C N^5
                              \|f\|_{\mathbb R}\|p\|_{\mathbb R}.
 \tag{16}
\]
This is the same full-normal product estimate as in the
whole-terminal anchor corollary. Equations (11),(14)--(16)
prove (9). The whole-terminal upper theorem then gives
the stated rate. \(\square\)

The scaled angular derivatives \(c_N'(j/N)(V_np_N)'(c_j)\),
where \(c_N(u)=2\cos(2\pi u+\pi/N)\), obey the same estimate.
Thus Lemma 2 initializes every fixed window of every actual
channel in (7), its gauge, and the original product, uniformly
in the endpoint parameters.

## 3. The exact gauged and recovered physical systems

Retain all matrices and polynomial gauges of the divided-
difference module. Put
\[
 R_*=6^r,\qquad k=33r,\qquad
 \mathcal F=V_n\operatorname{can}\mathcal W,\qquad
 Y=V_nB_{\boldsymbol\alpha,N}.
 \tag{17}
\]
Here \(\mathcal W\) is the \(R_*\)-vector of gauged ordinary
tensor channels. Its product component, denoted \(\mathcal F_*\)
after turning, has gauge exponent \(r\). The exact equations are
\[
 \{d(D_n)(J-c_0)I_{R_*}-(q-q^{-1})^2E(D_n)\}\mathcal F=0,
 \qquad
                   (D_n-2)^rY=\mathcal F_*.
 \tag{18}
\]
They are full-algebra identities. Their ordinary residuals
are \(P_N\) multiples; they need not vanish off-grid.
The module proves
\[
 \deg d=k,\quad \deg E_{ab}\le k,\quad
 d(Z)\longrightarrow(Z-2)^k,
 \tag{19}
\]
with uniformly bounded cleared coefficients for (4).
Their dependence on \(N^{-1}\) has bounded analytic expansions
near zero on each bounded complex parameter set. This follows
also directly from the displayed finite formulas: the apparent
quotients \((w_i-c_0)/(q-q^{-1})^2\) are removable and bounded,
and the source coefficient is \(O(N^{-2})\).

Fix \(n=\sigma m\ne0\), \(m=|n|\), and set
\[
                         M=km+1,\qquad \ell=rm.
 \tag{20}
\]
The two equations in (18) have physical shift orders \(M\)
and \(\ell\), respectively, in each direction.
For completeness their extreme phases and coefficients are
as follows. If \(d_k\) is the leading coefficient of \(d\),
the first equation has extremes
\[
 \begin{split}
 a_+(j)&=-d_k q^{-\sigma[k(2j+1)+mk^2]}
                                   \prod_{h=0}^{km} A(j+h)\ I_{R_*},\\
 a_-(j)&=-d_k q^{ \sigma[k(2j+1)-mk^2]}
                                   \prod_{h=0}^{km} B(j-h)\ I_{R_*}.
 \end{split}                                             \tag{21}
\]
For recovery they are
\[
 \begin{split}
 b_+(j)&=q^{-\sigma[r(2j+1)+mr^2]}
                                   \prod_{h=0}^{rm-1}A(j+h),\\
 b_-(j)&=q^{ \sigma[r(2j+1)-mr^2]}
                                   \prod_{h=0}^{rm-1}B(j-h).
 \end{split}                                             \tag{22}
\]
Indeed the exact extremes of \(D_n\) are
\[
 q^{-\sigma(2j+m+1)}\prod_{h=0}^{m-1}A(j+h),\qquad
 q^{\sigma(2j-m+1)}\prod_{h=0}^{m-1}B(j-h).
 \tag{23}
\]
Multiply \(k\) or \(r\) shifted copies to obtain (21)--(22).
The final \(J\) in (21) contributes its minus sign and the
last \(A\) or \(B\). All lower powers and the entire correction
\((q-q^{-1})^2E(D_n)\) have order at most \(km=M-1\);
none changes (21). The leading coefficient \(d_k\) tends
to \(1\), so no small scalar is introduced there.

On a buffered compact interval \(I\subset(0,1/2)\), divide
by the forward extremes and form the companions
\(\mathsf A_W(u)\), of dimension \(2MR_*\), and
\(\mathsf A_Y(u)\), of dimension \(2\ell\).
Their windows at row \(j\) are, respectively,
\[
 X_j^W=(\mathcal F(c_{j-M}),\ldots,\mathcal F(c_{j+M-1})),
 \qquad
 X_j^Y=(Y(c_{j-\ell}),\ldots,Y(c_{j+\ell-1})).
 \tag{24}
\]
Let \(\mathsf B(u)\) have only its final row nonzero. It
selects \(\mathcal F_*(c_j)\), the product component in the
current, central row of the \(W\) window, with coefficient
\(b_+(Nu)^{-1}\). It has size \(2\ell\) by \(2MR_*\).
All three matrices and their first \(u\) derivatives are
uniformly bounded on the fixed buffered interval.

Write \(Z_j^W,Z_j^Y\) for the same windows of derivatives
with respect to \(u\), evaluated at their shifted grid
arguments. The exact coupled system is
\[
 \begin{pmatrix}X^W\\Z^W\\X^Y\\Z^Y\end{pmatrix}_{j+1}
 =
 \begin{pmatrix}
 \mathsf A_W&0&0&0\\
 \mathsf A_W'&\mathsf A_W&0&0\\
 \mathsf B&0&\mathsf A_Y&0\\
 \mathsf B'&\mathsf B&\mathsf A_Y'&\mathsf A_Y
 \end{pmatrix}_{u=j/N}
 \begin{pmatrix}X^W\\Z^W\\X^Y\\Z^Y\end{pmatrix}_{j}.
 \tag{25}
\]
Primes in (25) mean scaled-coordinate coefficient derivatives.
The windows have their actual unequal sizes. In particular
no zero padding or dummy zero characteristic roots occur.

To justify the normal equations, apply the ordinary physical
operators to the canonical polynomials before evaluating.
The exact residual identity
\[
                         P_N(c_N(u))=4\sin^2(\pi Nu)
 \tag{26}
\]
annihilates both the residual value and its first \(u\)
derivative at every indicated grid row. This gives (25)
with all coefficient derivatives and all recovery forcing.
It does not assert an off-grid homogeneous equation.

## 4. Compact transfer with the multiple roots retained

Let \(x=2\cos(2\pi u)\), and let \(x_n(u,t),y(u,t)\)
be the exact limiting symbols of \(D_n,J\), with \(t\)
the physical shift variable. The principal \(W\) equation is
\[
                     (x_n-2)^k(y-2)I_{R_*};
 \tag{27}
\]
the recovery equation has principal symbol \((x_n-2)^r\).
The terminal characteristic source and bulk theorem show
that \(x_n-2\), after clearing its \(t^{-m}\), has precisely
the \(m\) separated roots \(\tau_{\ell,n}\), each double.
Also, with \(a(u)=\tan^2(\pi u)\),
\[
 y-2=-a(u)t^{-1}(t-1)^2.
 \tag{28}
\]
The root \(1\) is not terminal. At \(t=1\), one has \(y=2\)
and \(x_n=2+(-1)^n(x-2)\ne2\), as follows from the
ordered twist recurrence at \(y=2\) and its two initial
values \(x_0=x,\ x_1=4-x\).

Thus the scalar \(W\) companion has terminal blocks of
length \(2k=66r\) and one block of length two at \(1\).
After a fixed permutation, its principal matrix is a
direct sum of \(R_*\) copies of this scalar companion.
The recovery companion has terminal blocks of length \(2r\).
The repetition of channels does not concatenate those
Jordan chains. All distinct roots are separated, nonzero,
and analytic locally on the buffered interval. Their frames
and frame derivatives can be chosen uniformly bounded there.

Here are explicit quantitative details for the multiple-root
step. A scalar companion has a confluent Vandermonde frame
whose chain at a root \(t\) consists of
\[
       v(t),v'(t),\ldots,v^{(s-1)}(t)/(s-1)!,
       \qquad v(t)=(1,t,\ldots,t^{d-1})^{\mathsf T}.
 \tag{29}
\]
It gives a Jordan block with diagonal \(t\) and superdiagonal
one. Separation and the nonzero leading coefficient give
uniformly bounded frames, inverses and derivatives on each
fixed compact interval; finitely many overlapping frames
suffice if one does not choose a global analytic labeling.

Set
\[
                   \vartheta=N^{-1/(66r)}.
 \tag{30}
\]
Scale each chain of length \(s\le66r\) by
\(\operatorname{diag}(1,\vartheta,\ldots,\vartheta^{s-1})\).
Its superdiagonal becomes \(\vartheta\), and the condition
cost of all these scalings is at most
\(\vartheta^{-(66r-1)}\).
The finite-\(N\) diagonal companions differ from their
principal companions by \(O(N^{-1})\), uniformly with
fixed derivatives on the buffered interval. In the scaled
frame this error, and the change of frame over one row, are
therefore \(O(N^{-1}\vartheta^{-(66r-1)})=O(\vartheta)\).

For the four blocks of (25), make the additional constant
grade scaling
\[
                              (1,N,N,N^2).
 \tag{31}
\]
All nonzero off-diagonal blocks in (25) go from a lower
grade to a higher one. Each grade-one coupling thus gains
at least \(N^{-1}\), and the direct first-to-fourth coupling
gains \(N^{-2}\). Even a general bounded coupling between
different Jordan chains consequently costs at most
\[
                     C N^{-1}\vartheta^{-(66r-1)}
                                        =C\vartheta.
 \tag{32}
\]
This includes the actual source forcing and both derivative
couplings. It avoids treating a squared recovery equation
as a single unrelated high-multiplicity scalar equation.

The transformed one-step norm is at most
\[
       \max\{1,\max_\ell|\tau_{\ell,n}(u)|\}
                                      +C_I\vartheta.
 \tag{33}
\]
Since \(L_n\ge0\), its logarithm is at most
\(L_n(u)+C_I\vartheta\). The total frame condition at the
two ends costs at most
\(C_I N^{\,2+(66r-1)/(66r)}\); increasing a polynomial
power also covers a finite change of local frame.
Products of (33), followed by the Lipschitz Riemann-sum
estimate for \(L_n\) on \(I\), prove the compact bound
\[
 \|\mathcal T_{j_2,j_1}\|
 \le C_I N^{p_I}
       \exp\left\{N\int_{j_1/N}^{j_2/N}L_n(u)\,du
                          +C_I N^{1-1/(66r)}\right\}.
 \tag{34}
\]
It bounds every forward prefix, using the integral over the
whole interval if convenient. The estimate involves the
maximal modulus, not an assumed selected-branch coefficient.

## 5. The two endpoint strips and the unequal final windows

Put \(J_N=\lfloor(N-1)/2\rfloor\). The joint state (25)
starts at \(j=M\). Its \(W\) window uses only the fixed
rows \(0,\ldots,2M-1\); the \(Y\) window uses a subset
of these. By (8)--(9), its norm is at most
\[
                  C N^b(\|G_n\|_{\mathbb R}+\|H_n\|_{\mathbb R}).
 \tag{35}
\]
The fact that \(M\) is large is harmless: \(n,r\) are fixed.

For all joint centers
\[
                    M\le j\le J_N-M,\qquad
 d_j=\min\{j-M+1,J_N-M-j+1\}\ge1,
 \tag{36}
\]
every coefficient and first derivative in (25) is bounded by
\[
                              C_{n,r,A}(N/d_j)^B.
 \tag{37}
\]
We give the coefficient check because a factor \(N^B\) per
step would be insufficient. The original \(D_n\) is built
by a fixed number of products of \(J\) and spectral
multiplication. In a coefficient of the \(W\) operator,
every \(A(t),B(t)\) occurs with
\[
                         j-M+1\le t\le j+M-1.
 \tag{38}
\]
This follows by counting the shift before the last factor
in each ordered product. The final \(J\) in the highest
term attains the upper endpoint \(j+km=j+M-1\);
all other terms stay within it. Recovery uses the smaller
range with \(M\) replaced by \(\ell\).
Thus every coefficient row in (38) lies between \(1\)
and \(J_N-1\), at distance at least \(d_j\) from the
corresponding singular boundary.

Every nonzero denominator sine in (12) then has modulus
at least \(c\,d_j/N\). Also
\(\sin((t+1)\pi/N)\ge c\,d_j/N\).
One may use
\[
 |A(t)|+|B(t)|\le C(N/d_j)^2,\qquad
 |A(t)^{-1}|\le C(N/d_j)^4.
 \tag{39}
\]
First derivatives with respect to \(u=t/N\) cost only
further inverse sines, hence further powers of \(N/d_j\).
The cleared coefficients \(d,E\) are uniformly bounded
fixed-degree polynomials. Their leading coefficient
\(d_k\) is uniformly a unit. Equations (21)--(22) therefore
bound the normalized row coefficients and their derivatives
by (37). This also bounds the recovery selector and its
derivative. There is no additional standalone power of
\(N\) at each row.

Take the two strips of length \(\epsilon N+O_{n,r}(1)\).
On either strip, products of (37) are bounded by
\[
 C^K\prod_{a=1}^{K}(N/a)^B
       \le\exp\{C K\log(eN/K)\}
       \le\exp\{C N\epsilon\log(e/\epsilon)+O(\log N)\}.
 \tag{40}
\]
The constants in this estimate do not depend on
\(\epsilon\). Partial products obey the same bound.

The final joint center \(j=J_N-M\) generates the \(W\)
value at \(J_N\), but generates \(Y\) only through
\(J_N-M+\ell\). This discrepancy must not be ignored.
Continue only the exact recovery equation and its first
normal equation for
\[
                        J_N-M+1\le j\le J_N-\ell .
 \tag{41}
\]
There are \(M-\ell\) such additional steps, a fixed number.
All required \(\mathcal F_*(c_j)\) and its angular normal
are already available from the completed \(W\) propagation.
The coefficients in these last recovery rows are at most
a polynomial in \(N\), by the same sine-distance argument
with \(\ell\). They multiply the bound already obtained,
with only a further polynomial cost. Their last output is
the actual \(Y(c_{J_N})\).

At odd \(N\), \(c_{J_N}=-2\) is the simple node; its angular
derivative is zero and no spectral normal there is required.
At even \(N\), the last node is double and its first normal
is retained. All coefficient evaluations remain at most
\(J_N-1\); no singular next row was invoked.

## 6. Whole-interval assembly and derivatives

Apply (40) to the left strip, (34) to the fixed intervening
compact interval, and (40) to the right strip. Then use
the finite recovery completion (41).
Since \(L_n\ge0\), the same total bound controls every
intermediate value and scaled angular normal.
Replacing either compact endpoint by a neighboring grid
point changes its exponent by \(O_\epsilon(1)\).
Together with (35), this bounds every physical value and
required angular first normal of \(Y\) by the right side
of (6).

The ordinary canonical polynomial is recovered with the
stable full-Hermite inequality
\[
 \|Y\|_{\mathbb R}\le(2N-1)\max_{\rm physical}|Y|
       +2\max_{\rm angular}|\partial_tY(-2\cos t)|.
 \tag{42}
\]
Here \(t=\pi-2\pi u-\pi/N\), so its angular derivative
is \(-1/(2\pi)\) times the scaled derivative used in
(25). The paired lifts and odd simple node therefore
give exactly the data required by (42). This proves (6).

For fixed \(\epsilon\), the whole-terminal upper theorem
gives an initial limsup of at most \(\mathcal I_n\).
Divide the logarithm of (6) by \(N\), take the upper limit,
and only then send \(\epsilon\) to zero. The endpoint
loss tends to zero and the improper characteristic integral
converges. This proves (5) for \(n\ne0\).
For \(n=0\), \(V_0=I\), and the polynomial input bound
already proves (5).

All estimates were uniform on arbitrary fixed bounded
complex parameter polydisks. Cauchy's formula on a
slightly larger such polydisk gives the same exponential
rate for every fixed parameter derivative. Ordinary
Markov inequalities for the degree-\(D\) output add only
polynomial factors for fixed spectral derivatives.
This establishes the derivative assertion without
discarding any original normal channel.

The proof pays two independent upper budgets:
the actual fixed-row source initialization, bounded by
\(\mathcal I_n\), and subsequent maximal-characteristic
transport, bounded by \(\mathcal I_n\). Nothing here shows
that both budgets are attained or that either can be
removed. The characteristic determinant alone would not
justify even this conclusion without (9), the regular
extreme coefficients, and the forced recovery.

## 7. Direct sources and scope

All five complete direct sources have been read at the
following pins, with the used implications checked:

* [Exact product module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093:
  six ordinary channels, aliases, polynomial gauge, degree
  \(33r\), cleared matrices, original turn and forced recovery.
* [Whole-terminal upper bound](research_whole_terminal_characteristic_upper_bound.md),
  SHA256 ee91f066e0e5b0eb60e4076ba2a2090e1439787c57caf6eaaa09341138d05176:
  actual \(G_n,H_n\) initialization and rates, fixed-row
  original equations, full-Hermite and coherent trace bounds,
  integrability and nonnegativity of \(L_n\).
* [Physical bulk transfer](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_twist_bulk_transfer_bound.md),
  SHA256 fca96865315f21dc9961be89061cc6c3a292b2b563e7ded756e86c3438ef5bde:
  exact signed physical operators and extremes, ideal
  residuals, separated double terminal roots and the
  value/normal transfer convention.
* [Original finite-band operators](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  full algebra and Frobenius transport, ordered twist
  recurrence, and the polynomial \(J\) norm.
* [Whole endpoint products](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  uniform polynomial real norm for fixed ordinary microscopic
  endpoint products on bounded complex parameter sets.

No selected-branch lower coefficient, volume gap, arbitrary
tree closure, or equality with a terminal source is claimed.
All crossing phases, tensor channels and first normals were
retained before taking upper bounds.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build
was run. Adopted notes and public manuscripts are unchanged.
