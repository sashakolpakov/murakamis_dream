# Quarter-turns with a moving meridian: exact coefficients and spectral bounds

A quarter-turn of a two-strand tangle bends one incoming strand into an outgoing strand and one outgoing strand into an incoming strand. In the quantum calculation this changes the ordered tensor product on which the tangle acts. When the meridian parameter moves away from its complete value, the two possible strand colors are dual but unequal. The turn must therefore retain the evaluation maps and the braiding that identifies the two orders of an opposite-color pair.

This note computes that operation in a fixed polynomial basis. Its answer is a reversal of the complete Newton coefficients, multiplied by an explicit paired sine product. The paired product and its inverse are uniformly bounded before the first ordinary-color resonance. A further argument controls both the values and the first derivatives at the repeated complete Casimir nodes. On a small fixed complex parameter disk, the deformed turn has the same exponential spectral norm as the complete turn of the same polynomial.

The proof uses the actual three-strand intertwiner space, including its repeated channels. The exact compiler and its normalization are described in [the moving-meridian Newton compiler](actual_main_meridian_newton_compiler.md); the complete crossing matrix is the one in [the canonical Newton source calculation](actual_newton_twist_canonical_graph.md). The calculations needed here are included below. The final section distinguishes these operator estimates from a bound for a whole knot contraction.

## 1. The fixed polynomial basis and the comparison theorem

Fix an integer level $N\ge2$, and put
\[
d=N-1,\qquad \theta=\frac\pi N,\qquad q=e^{i\theta},\qquad
Q=q^2,\qquad \rho=q-q^{-1}.
\tag{1}
\]
The complex variable $s$ describes the microscopic meridian displacement: the meridian parameter is $M=q^s$. We use the two dual highest roots
\[
x=-q^{-1}q^s,\qquad y=-q^{-1}q^{-s}.
\tag{2}
\]
A plus sign will mean the module with root $x$, and a minus sign the module with root $y$. We first work on a fixed disk $|s|\le R<1$.

For $0\le n<N$, define
\[
\begin{aligned}
S_n&=\prod_{r=1}^n2\sin(r\theta),\qquad
c_j(s)=2\cos((2j+1-2s)\theta),\qquad c_j=c_j(0),\\
e_n^s(z)&=\frac1{S_n^2}\prod_{j=0}^{n-1}(c_j(s)-z),
\qquad e_n(z)=e_n^0(z).
\end{aligned}
\tag{3}
\]
An empty product is one. The $e_n$ form a basis of the vector space of polynomials of degree less than $N$. **Fixed polynomial coordinates** mean that a polynomial $f=\sum_{n=0}^d\alpha_ne_n$ is kept in this basis while its argument is the actual moving Casimir. They do not identify the moving quotient algebra with the complete quotient algebra.

The scalar factors in the answer are
\[
\begin{aligned}
P_n(s)&=\prod_{r=1}^n\frac{\sin((r-s)\theta)}{\sin(r\theta)},\\
H_N(s)&=P_d(s)=\frac{\sin(\pi s)}{N\sin(\pi s/N)},\\
W_n(s)&=P_n(s)P_n(-s)
 =\prod_{r=1}^n\left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right).
\end{aligned}
\tag{4}
\]
The quotient defining $H_N$ is assigned its removable value one at zero. Let $\mathcal R e_n=e_{d-n}$ be complete Newton reversal, and let $\mathcal D_s e_n=W_n(s)e_n$.

**Theorem.** In the normalized physical coordinates defined in Section 2, every orientation type of the forward quarter-turn has the form
\[
\boxed{\displaystyle
\mathscr T_s^{\mathrm{fix}}
  =\frac{\gamma_N(s)}{H_N(s)}\,\mathcal R\mathcal D_s,
\qquad \gamma_N(s)\in\{1,q^{-s^2/2},q^{s^2/2}\}.}
\tag{5}
\]
The six domains and their scalars are specified in Section 3. In particular, a turn from a same-color endomorphism to the indicated mixed-order morphism has scalar $q^{-s^2/2}$. This formula is exactly even in $s$, including its scalar.

For every fixed $R<1$, there are positive constants independent of $N,n,s$ such that
\[
\left(\frac{\sin\pi R}{\pi R}\right)^2
 \le |W_n(s)|\le
\left(\frac{\sinh\pi R}{\pi R}\right)^2,
\qquad |s|\le R.
\tag{6}
\]
Also
\[
W_n(s)W_{d-n}(s)=H_N(s)^2.
\tag{7}
\]
Consequently (5) and its inverse are uniformly comparable to complete reversal in every diagonal weighted coefficient norm. More explicitly, if the weights are any positive numbers and $1\le p\le\infty$,
\[
C_R^{-1}\|\mathcal R f\|_{p,w}
 \le\|\mathscr T_s^{\mathrm{fix}}f\|_{p,w}
 \le C_R\|\mathcal R f\|_{p,w}.
\tag{8}
\]
The reversal in this estimate is essential when the weights are not symmetric under $n\mapsto d-n$.

To state the spectral comparison, put $m=\lfloor d/2\rfloor$. The distinct complete Casimir nodes are $c_0,\ldots,c_m$. They are all double if $N$ is even; if $N$ is odd, only $c_m=-2$ is simple. Denote the double-node index set by
\[
\mathcal I_{\mathrm{dbl}}=
\begin{cases}
\{0,\ldots,m\},&N\text{ even},\\
\{0,\ldots,m-1\},&N\text{ odd}.
\end{cases}
\]
For a canonical polynomial of degree less than $N$, define its full spectral-jet norm by
\[
\|f\|_{\mathrm J}
=\max\left\{\max_{0\le j\le m}|f(c_j)|,
                  \max_{j\in\mathcal I_{\mathrm{dbl}}}|f'(c_j)|\right\}.
\tag{9}
\]
The prime here is differentiation in the polynomial variable. These data determine the polynomial. There is an absolute constant $C$ such that
\[
\boxed{\displaystyle
C^{-1}N^{-7}\|\mathcal Rf\|_{\mathrm J}
\le\|\mathscr T_s^{\mathrm{fix}}f\|_{\mathrm J}
\le CN^7\|\mathcal Rf\|_{\mathrm J},\qquad |s|\le\frac1{16}.}
\tag{10}
\]
All fixed derivatives in $s$ have polynomial bounds on smaller disks. Thus the polynomial factor in (10) does not change the exponential rate of the complete turn of this particular input. It does not bound the complete turn itself by a polynomial operator norm on arbitrary inputs.

## 2. The physical turn and its three-strand calculation

### 2.1. Modules, dualities, and the mixed-order reference

Write $[a]=\sin(a\theta)/\sin\theta$. The nilpotent module $V_x$ has basis $v_0,\ldots,v_d$ and actions
\[
Kv_a=xQ^{-a}v_a,\qquad Fv_a=v_{a+1},\qquad
Ev_a=\varepsilon_a(x)v_{a-1},\qquad
\varepsilon_a(x)=[a][a-s].
\tag{11}
\]
Vectors outside the displayed index range are zero. The module $V_y$, with basis $w_a$, is obtained by replacing $s$ by $-s$. If $\varphi_a$ is the basis dual to $v_a$, the actual duality map is
\[
J_xw_a=\gamma_a(x)\varphi_{d-a},\qquad
\gamma_a(x)=(-x)^aQ^{a(a+1)/2}.
\tag{12}
\]
Here $\gamma_a$ is a duality coefficient; it is unrelated to the scalar $\gamma_N(s)$ in (5).

We use $\Delta E=E\otimes K+1\otimes E$,
$\Delta F=F\otimes1+K^{-1}\otimes F$, and
\[
\Omega=\rho^2FE+qK+q^{-1}K^{-1}
      =\rho^2EF+qK^{-1}+q^{-1}K.
\tag{13}
\]
Inserting (12) into the evaluation and coevaluation maps gives the following entry formula for turning an endomorphism of $V_x\otimes V_x$:
\[
\mathcal T_x(A)^{jb}_{ak}
 =\frac{\gamma_a(x)}{\gamma_b(x)}A^{d-a,j}_{k,d-b}.
\tag{14}
\]
Its domain is $V_y\otimes V_x$, and its codomain is $V_x\otimes V_y$. Turning an endomorphism of $V_x\otimes V_y$ instead gives
\[
\mathcal U_{x,y}(A)^{jb}_{ak}
 =\frac{\gamma_a(x)}{\gamma_b(y)}A^{d-a,j}_{k,d-b},
\tag{15}
\]
an endomorphism of $V_y\otimes V_x$. These formulas specify which strand is bent and in which direction.

For a morphism between the two opposite-color orders we choose $V_x\otimes V_y$ as reference. Let $r_0$ be the complete checked crossing polynomial, including its scalar and its coefficients at repeated nodes. The carrier from $V_x\otimes V_y$ to $V_y\otimes V_x$ is
\[
G_{-+}=\check R_{x,y}\,r_0(\Omega_{x,y})^{-1},\qquad G_{+-}=I.
\tag{16}
\]
The inverse exists in the constant opposite-color Casimir algebra. The normalization gives $G_{-+}(0)=I$ in the complete physical bases. The polynomial endomorphism representing (14) is therefore
\[
\widehat{\mathcal T}_s(f)
 =\mathcal T_x(f)\check R_{x,y}r_0(\Omega_{x,y})^{-1}.
\tag{17}
\]
The order of these factors is part of the definition. No carrier is inserted into (15), since its source and target are already endomorphism spaces.

We keep the complete balanced basis fixed during the deformation. Its diagonal change from (11) is
\[
|a\rangle=\delta_av_a,\qquad
\delta_a=\frac{\rho^a}{(Q;Q)_a},\qquad
(Q;Q)_a=\prod_{r=1}^a(1-Q^r).
\tag{18}
\]
At $s=0$, with $x_0=-q^{-1}$, the finite product identity
\[
(Q;Q)_a(Q;Q)_{d-a}
 =N(-1)^aQ^{a(a+1)/2}
\]
implies
\[
\delta_a\delta_{d-a}\gamma_a(x_0)
 =\frac{\rho^d}{N}x_0^a.
\tag{19}
\]
Thus (14) has precisely the balanced duality ratios of the complete turn. Its transpose convention agrees on Casimir polynomials, which are symmetric in that complete balanced realization. This verifies the complete normalization before deforming it.

### 2.2. The full intertwiner space

Consider intertwiners from $V_x$ to $V_x\otimes V_x\otimes V_y$. Let $W_d$ be the middle-degree space of the first two factors, spanned by $v_j\otimes v_{d-j}$. A vector $w\in W_d$ determines the highest vector
\[
H_L(w)=\sum_{c=0}^d
 \frac{(-y)^cQ^{-c(c-1)/2}}{\prod_{r=1}^c\varepsilon_r(y)}
 E_{12}^cw\otimes w_c.
\tag{20}
\]
Indeed, writing this as $\sum z_c\otimes w_c$, the highest-vector equation is
$z_{c+1}=-yQ^{-c}E_{12}z_c/\varepsilon_{c+1}(y)$. The final equation is $E_{12}^Nw=0$. Its total highest root is $x^2yQ^{-d}=x$, so its full $F$-string defines an intertwiner $I_w$ from $V_x$. All $\varepsilon_r(x)$ and $\varepsilon_r(y)$, $1\le r<N$, are nonzero on $|s|<1$. The commutator relations verify the $F$-string, and extraction at third color zero recovers $w$. This describes the whole $N$-dimensional intertwiner space, including the repeated-channel directions.

Use the coordinate vectors $\mathbf e_j$ for $W_d$ in the fixed gauge $\delta_j\delta_{d-j}$. Let $\mathsf A_s$ and $\mathsf C_s$ denote the actions of $\Omega_{12}$ and $\Omega_{23}$ on these coordinates. Put $\mathsf D_s=\operatorname{diag}(P_j(s))$. Direct extraction at third color zero in (20) gives
\[
\mathsf C_s=\mathsf D_s^{-1}\mathsf C_0\mathsf D_s,
\qquad (\mathsf C_0)_{jj}=c_j,\qquad
(\mathsf C_0)_{j-1,j}=\rho^2[j]^2.
\tag{21}
\]
Only third colors zero and one can contribute to this extraction. Their $F_2E_2$ terms cancel; what remains is
$-\rho^2yF_2E_1K_2$, together with
$qK_2K_3+q^{-1}K_2^{-1}K_3^{-1}$. In the fixed balanced basis these are the diagonal $c_j$ and superdiagonal $\rho^2[j][j-s]$, proving (21).

For the first pair, insertion of (11) into (13) gives
\[
\begin{aligned}
(\mathsf A_s)_{jj}&=(\mathsf A_0)_{jj}+\rho^2[s]^2qQ^j,\\
(\mathsf A_s)_{j-1,j}&=-\rho^2Q^j[j][j-s],\\
(\mathsf A_s)_{j,j-1}&=-\rho^2Q^j[j][j+s],\\
(\mathsf A_0)_{jj}&=4qQ^j-q(1+Q)Q^{2j}.
\end{aligned}
\tag{22}
\]
In particular,
\[
\mathsf D_s\mathsf A_s\mathsf D_s^{-1}
 =\mathsf A_0+\rho^2[s]^2\mathsf K,
\qquad \mathsf K_{jj}=qQ^j,\qquad \mathsf K_{j,j-1}=Q^j.
\tag{23}
\]
The offdiagonal identity here is $[j-s][j+s]=[j]^2-[s]^2$.

### 2.3. The crossing conjugation, including its last column

Let $\mathsf R_0=r_0(\mathsf C_0)$, and let $J\mathbf e_j=\mathbf e_{d-j}$. The complete crossing matrix is
\[
(\mathsf R_0)_{ij}
 =\kappa_0(-1)^jq^{j+i^2}{j\brack i}_Q\quad(i\le j),
\qquad \kappa_0=q^{d^2/2},
\tag{24}
\]
with zero entries when $i>j$. The Gaussian binomial coefficient is
${j\brack i}_Q=(Q;Q)_j/((Q;Q)_i(Q;Q)_{j-i})$.
Its complete conjugation identity is
\[
\mathsf R_0^{-1}\mathsf A_0\mathsf R_0=\mathsf C_0^T.
\tag{25}
\]
Here is an entrywise check that also keeps the end rows. For $U=\mathsf R_0$, the three ratios needed in $\mathsf A_0U=U\mathsf C_0^T$ are
\[
\begin{aligned}
\frac{U_{i-1,j}}{U_{ij}}
 &=q^{-2i+1}\frac{1-Q^i}{1-Q^{j-i+1}},\\
\frac{U_{i+1,j}}{U_{ij}}
 &=q^{2i+1}\frac{1-Q^{j-i}}{1-Q^{i+1}},\\
\frac{U_{i,j+1}}{U_{ij}}
 &=-q\frac{1-Q^{j+1}}{1-Q^{j-i+1}}.
\end{aligned}
\tag{26}
\]
Substitute (22), multiply through by the displayed denominators, and use $Q=q^2$. The resulting polynomial identity proves every interior entry. The boundary terms vanish by $[0]=[N]=0$ and $1-Q^N=0$, so the same identity proves the first and last rows. No simple-eigenvalue assumption is involved.

The perturbation in (23) has another exact conjugation:
\[
\mathsf R_0^{-1}\mathsf K\mathsf R_0
 =-\mathsf S_{\mathrm{low}}+(-1)^N\mathbf e_0\mathbf e_d^T,
\tag{27}
\]
where $\mathsf S_{\mathrm{low}}\mathbf e_j=\mathbf e_{j+1}$ for $j<d$, and its last column is zero. For $j<d$, the $i$-th entry of $\mathsf K\mathsf R_0\mathbf e_j$, after removing its common scalar, is
\[
Q^i{j\brack i}_Q+{j\brack i-1}_Q={j+1\brack i}_Q.
\]
It is therefore the negative of column $j+1$ of $\mathsf R_0$. In the last column the same identity gives ${N\brack i}_Q=0$ for $1\le i<N$, whereas its zeroth entry is $(-1)^N\kappa_0$. Since $\mathsf R_0\mathbf e_0=\kappa_0\mathbf e_0$, this proves (27), including the last-column term.

Set $\mathsf V_s=J\mathsf R_0^{-1}\mathsf D_s$. Equations (21), (23), (25), and (27) give
\[
\mathsf V_s\mathsf C_s\mathsf V_s^{-1}=\mathsf C_0^T,
\qquad
\mathsf V_s\mathsf A_s\mathsf V_s^{-1}=\mathsf L_s,
\tag{28}
\]
where
\[
\begin{aligned}
(\mathsf L_s)_{kk}&=c_k,\\
(\mathsf L_s)_{k-1,k}
 &=-4\sin((k-s)\theta)\sin((k+s)\theta)\quad(1\le k\le d),\\
(\mathsf L_s)_{d,0}&=(-1)^{N+1}4\sin^2(s\theta).
\end{aligned}
\tag{29}
\]
All other entries vanish. The bottom-left entry is retained: it is precisely the term that would be lost by treating the deformed algebra as the complete one.

### 2.4. Bending the strand identifies the physical coordinates

It remains to show that the preceding matrix change is the actual turn with (12) and (16). Apply (20) to the endpoint vector $\mathbf e_d$. Only $E_1K_2$ acts, and $\varepsilon_{N-r}(x)=\varepsilon_r(y)$, giving
\[
H_L(\mathbf e_d)=\sum_{c=0}^d
 (-1)^cQ^{-c(c+1)/2}
 v_{d-c}\otimes v_0\otimes w_c.
\tag{30}
\]
In the checked braiding of the last two factors, the first input is $v_0$, so every nonzero transfer term is absent. If $\alpha=d+s$, its zero-transfer coefficient is
$\kappa_{xy}q^{-\alpha c}$, where
$\kappa_{xy}=q^{(d^2-s^2)/2}$. Multiplying by the coefficient in (30) gives
$\kappa_{xy}\gamma_c(x)^{-1}$. Thus
\[
\check R_{23}I_{\mathbf e_d}
 =\kappa_{xy}(\operatorname{coev}_{x,y}\otimes I_x).
\tag{31}
\]
Equality on the generating highest vector proves equality of the intertwiners. The balanced gauges of $\mathbf e_0$ and $\mathbf e_d$ coincide, so this scalar is unchanged by (18).

For any polynomial $f$ in the first-pair Casimir, insert $f$ into (31) and apply the evaluation–coevaluation identity. In the coordinate convention of (14), the result is
\[
[\mathcal T_x(f)\check R_{x,y}]_{23}I_{\mathbf e_d}
 =\kappa_{xy}I_{f(\mathsf A_s)\mathbf e_0}.
\tag{32}
\]
This is the strand-bending identity with all scalars retained. Let
$\widehat{\mathcal T}_s(f)=\sum\alpha_ke_k$. The left side is
$(\widehat{\mathcal T}_s(f)r_0)(\mathsf C_s)\mathbf e_d$. The bidiagonal matrix (21) gives
\[
e_k(\mathsf C_s)\mathbf e_d=P_k(-s)\mathbf e_{d-k},
\qquad P_k(-s)P_{d-k}(s)=H_N(s).
\tag{33}
\]
Using $r_0(\mathsf C_s)=\mathsf D_s^{-1}\mathsf R_0\mathsf D_s$ in (32) therefore yields
\[
\boxed{\displaystyle
\operatorname{coeff}\widehat{\mathcal T}_s(f)
 =\frac{\kappa_{xy}}{H_N(s)}\mathsf V_s f(\mathsf A_s)\mathbf e_0
 =\frac{q^{-s^2/2}}{H_N(s)}f(\mathsf L_s)\mathbf e_d.}
\tag{34}
\]
For the last equality, use $\mathsf V_s\mathbf e_0=\kappa_0^{-1}\mathbf e_d$. This proves a coefficient formula for the entire physical morphism, rather than for a selected boundary matrix entry.

Now evaluate (34) on the fixed polynomial $e_n$. The reflection $c_{d-n}=c_n$ cancels the diagonal at each step of its Newton product. The only remaining path moves successively from $\mathbf e_d$ to $\mathbf e_{d-n}$, and its $n$ factors are the paired sine ratios in (4). Hence
\[
e_n(\mathsf L_s)\mathbf e_d=W_n(s)\mathbf e_{d-n},
\qquad 0\le n<N.
\tag{35}
\]
The bottom-left entry in (29) cannot act on this path: reaching $\mathbf e_0$ already takes $d$ steps, and a canonical polynomial has degree at most $d$. This explains why it remains in the physical matrix but does not appear as an additional term in (35). Equations (34)–(35) prove (5) for the specified same-color turn.

They also give a useful fixed-coordinate functional calculus:
\[
\operatorname{coeff}\widehat{\mathcal T}_s(f)
 =\frac{\kappa_{xy}}{H_N(s)}J\mathsf R_0^{-1}
 f(\mathsf A_0+\rho^2[s]^2\mathsf K)\mathbf e_0.
\tag{36}
\]
Its dependence on $s$ is exactly even. This identity does not discard the deformation of multiplication.

## 3. The six ordered orientation types

The signs in an ordered pair record the modules, not a choice of square root for a scalar. There are four turns in the orbit beginning with a same-color endomorphism, and two turns between opposite-color endomorphism spaces. We now determine their carriers and scalars.

First consider (15). On the degree-$t$ block of an opposite-color tensor product, ordered by $v_a\otimes w_{t-a}$, the characteristic and minimal polynomial of the Casimir are
\[
\prod_{j=0}^t(z-c_j),\qquad 0\le t\le d.
\tag{37}
\]
The characteristic identity follows from the generic highest-vector decomposition and continuation of that polynomial identity. The tridiagonal matrix is cyclic: its offdiagonal factors have indices between $1$ and $d$, and their color factors are $[r-s]$ or $[r+s]$, which do not vanish on $|s|<1$. Thus (37) retains repeated roots and their derivative data.

It follows that $e_n(\Omega)$ vanishes on this block when $n>t$. For $n<t$, its first-color bandwidth is at most $n$, so its extreme entry is zero. When $n=t$, the unique path from first color $t$ to zero gives
\[
(e_t(\Omega_{x,y}))_{(0,t);(t,0)}=M^{-2t}P_t(s).
\tag{38}
\]
For example, before multiplying by the leading coefficient $(-1)^t/S_t^2$, the path product is
$\rho^{2t}(y/x)^t\prod_{a=1}^t\varepsilon_a(x)$; its powers of $Q$ cancel. This proves (38) and gives an extractor for every Newton coefficient without dividing by eigenvalue differences.

The entry formula (15) now proves
\[
\mathcal U_{x,y}(e_n(\Omega_{x,y}))
 =\frac{P_n(-s)}{P_{d-n}(-s)}e_{d-n}(\Omega_{y,x})
 =\frac{W_n(s)}{H_N(s)}e_{d-n}(\Omega_{y,x}).
\tag{39}
\]
Here are both degree bounds. The source bandwidth makes the output vanish on all blocks of degree below $d-n$, so it is divisible by $e_{d-n}$. On the middle block, column $a$ of its first row is proportional to
$(e_n(\Omega_{x,y}))_{(d-a,0);(d-a,0)}$, which vanishes when $a>d-n$ by (37). The target first row is cyclic, and a polynomial of degree $r<N$ has a nonzero entry in column $r$ from its unique outermost path. The output degree is therefore at most $d-n$. Finally put $t=d-n$ in (38): the source increasing path in (15) contributes $P_n(-s)$, its duality contributes $M^{2t}$, and the target path contributes $M^{2t}P_t(-s)$. Their ratio is (39). Interchanging $x,y$ gives the other opposite-color turn; its scalar is the same by (33).

Next, two successive applications of the physical currying formula have entries
\[
\frac{\gamma_a(x)\gamma_k(x)}{\gamma_b(x)\gamma_j(x)}
 A^{d-k,d-a}_{d-b,d-j}.
\tag{40}
\]
This is the dual endomorphism under the reversed tensor-order identification. The antipode fixes the Casimir, as the equality of the two expressions in (13) verifies. Hence the double turn sends $f(\Omega_{x,x})$ to the same polynomial $f(\Omega_{y,y})$. A double-dual pivotal conjugation acts trivially on this centralizer. In fixed polynomial coordinates the second turn is consequently the inverse of the first; there is no change from $e_n^s$ to $e_n^{-s}$ to insert into these fixed coordinates.

There is one more scalar when the opposite-color reference order is swapped. Write $G'=\check R_{y,x}r_0^{-1}$. To compute it with the repeated-channel coefficients retained, temporarily take generic highest weights
\[
\alpha=d+s+\epsilon/2,\qquad \beta=d-s+\epsilon/2.
\]
On channel $j$, multiplying the two highest-vector braid scalars gives the monodromy eigenvalue
\[
q^{\alpha\beta-2j(\alpha+\beta)+2j(j-1)}.
\tag{41}
\]
The factorial ratios of the two braid scalars cancel. Replacing the two weights by $d+\epsilon/2,d+\epsilon/2$ keeps every Casimir node unchanged and changes the exponent only by $-s^2$. The resulting generic polynomial identity extends to $\epsilon=0$: the divided differences converge with the physical matrices, and the nondegenerate moment pairing determines the full polynomial, including its repeated-node coefficients. Therefore
\[
\check R_{y,x}\check R_{x,y}
 =q^{-s^2}r_0(\Omega)^2,
\qquad G'G_{-+}=q^{-s^2}I.
\tag{42}
\]
For a morphism $\mathcal B:V_x\otimes V_y\to V_y\otimes V_x$, the fixed-reference polynomial is $G_{-+}^{-1}\mathcal B$. Its natural sign-reversed presentation is $\mathcal BG'$. Conjugating the latter by $G_{-+}$ shows that the fixed-reference coefficient vector is $q^{s^2}$ times the natural one. This is the scalar correction that would be missed by simply interchanging $s$ and $-s$.

Define
\[
\mathcal M_s=H_N(s)^{-1}\mathcal R\mathcal D_s.
\tag{43}
\]
The reflection identity (7), proved below directly from the finite sine product, gives $\mathcal M_s^2=I$. Equations (34), (39), (40), and (42) now give the complete orientation table. Each row concerns the \(N\)-dimensional intertwiner space represented by Casimir polynomials, rather than every linear map on the tensor product. In the first four rows a mixed-order morphism is expressed using the fixed reference (16).

| Input space | Output space after the forward turn | Coefficient map |
| --- | --- | --- |
| $\operatorname{End}(V_x\otimes V_x)$ | $\operatorname{Hom}(V_y\otimes V_x,V_x\otimes V_y)$ | $q^{-s^2/2}\mathcal M_s$ |
| $\operatorname{Hom}(V_y\otimes V_x,V_x\otimes V_y)$ | $\operatorname{End}(V_y\otimes V_y)$ | $q^{s^2/2}\mathcal M_s$ |
| $\operatorname{End}(V_y\otimes V_y)$ | $\operatorname{Hom}(V_x\otimes V_y,V_y\otimes V_x)$ | $q^{s^2/2}\mathcal M_s$ |
| $\operatorname{Hom}(V_x\otimes V_y,V_y\otimes V_x)$ | $\operatorname{End}(V_x\otimes V_x)$ | $q^{-s^2/2}\mathcal M_s$ |
| $\operatorname{End}(V_x\otimes V_y)$ | $\operatorname{End}(V_y\otimes V_x)$ | $\mathcal M_s$ |
| $\operatorname{End}(V_y\otimes V_x)$ | $\operatorname{End}(V_x\otimes V_y)$ | $\mathcal M_s$ |

This also identifies the inverse of each map. The four-turn cycle returns to its initial polynomial, with both the reversal and the carrier scalars accounted for.

## 4. Uniform paired-product bounds and the bulk correction

Euler's sine product gives, for $1\le r<N$,
\[
\frac{\sin((r-s)\pi/N)\sin((r+s)\pi/N)}{\sin^2(r\pi/N)}
 =\prod_{k\in\mathbb Z}\left(1-\frac{s^2}{(r+kN)^2}\right).
\tag{44}
\]
The paired product is absolutely convergent. As $r$ ranges from $1$ to $n<N$, all the integers $r+kN$ are distinct and nonzero. For $|s|\le R<1$, bound each factor below by $1-R^2/(r+kN)^2$ and above by $1+R^2/(r+kN)^2$. Enlarging the subset to all nonzero integers decreases the lower product and increases the upper product. The two resulting Euler products are precisely those in (6).

The finite sine identity in (4) also gives $P_d(-s)=P_d(s)=H_N(s)$. Reflecting a suffix by $r\mapsto N-r$ gives
\[
P_n(s)P_{d-n}(-s)=H_N(s),\qquad
W_n(s)W_{d-n}(s)=H_N(s)^2.
\tag{45}
\]
In particular $H_N$, its inverse, and the factors $q^{\pm s^2/2}$ are uniformly bounded on the fixed disk. Formula (5) acts on each reversed coordinate separately, proving (8), as well as the inverse estimate. This proof applies to arbitrary positive diagonal weights; it makes no assumption about the size of their reversal ratios.

There is a sharper interior expansion. Fix $\delta>0$. Uniformly for
$\delta N\le n\le(1-\delta)N$ and $|s|\le R<1$,
\[
\log\frac{W_n(s)}{H_N(s)}
 =\frac{\pi s^2}{N}\cot(\pi n/N)+O_{R,\delta}(N^{-2}).
\tag{46}
\]
The logarithm is the holomorphic branch with value zero at $s=0$. To prove (46) without expanding any endpoint factor, use the symmetry in (45). If $N=2m+1$, then $H_N=W_m$. If $N=2m+2$, then $H_N=W_m\cos(s\theta)$. Thus the logarithm in (46) is a signed sum between $n$ and the midpoint, with a possible half-weight middle term. Throughout that interval the sine denominators stay bounded away from zero, and
\[
\log\left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right)
 =-\frac{\pi^2s^2}{N^2}\csc^2(\pi r/N)+O_{R,\delta}(N^{-4}).
\]
The summed remainder is $O(N^{-3})$. The Riemann sum, with endpoint error $O(N^{-2})$, is
\[
-\frac{\pi^2s^2}{N}\int_{1/2}^{n/N}\csc^2(\pi t)\,dt
 =\frac{\pi s^2}{N}\cot(\pi n/N),
\]
which proves (46). The bounds hold on a slightly larger complex disk, so Cauchy's formula proves the corresponding expansion for every fixed $s$-derivative on smaller disks.

For the first row of the orientation table, the multiplier on the reversed $n$-th coefficient is therefore
\[
\exp\left[\frac{\pi s^2}{N}
  \left(\cot(\pi n/N)-\frac i2\right)+O_{R,\delta}(N^{-2})\right].
\tag{47}
\]
The types with $q^{s^2/2}$ have $+i/2$ instead; the two opposite-color endomorphism turns have no Gaussian phase. At indices near the ends, (6) still applies, but (46) makes no $1+O(N^{-1})$ assertion.

## 5. A positive kernel on the distinct Casimir nodes

We next prove the value estimate that will control the repeated-node derivatives by duality. Restrict temporarily to polynomials of degree at most $m=\lfloor d/2\rfloor$. Their values at the distinct nodes determine them. Put $t_r=2\sin(r\theta)$. The evaluation matrix is
\[
E_{jn}=e_n(c_j)=\frac{S_{j+n}}{S_{j-n}S_n^2}\quad(n\le j\le m),
\qquad E_{jn}=0\quad(n>j).
\tag{48}
\]
Indeed, $c_r-c_j=t_{j+r+1}t_{j-r}$. Every factorial index in (48) is below $N$, and the diagonal is positive.

Let $\mathsf S\mathbf e_n=\mathbf e_{n+1}$ for $n<m$, with last column zero. Multiplication by $z$, reduced modulo the polynomial of the distinct nodes, has diagonal $c_n$ and subdiagonal $-a_{n+1}$, where $a_r=t_r^2$. Call this matrix $Z$, and write $\Lambda=\operatorname{diag}(c_0,\ldots,c_m)$. Then $EZ=\Lambda E$.

The conjugated coefficient shift has an explicit positive kernel:
\[
L=E\mathsf S E^{-1},\qquad
L_{jl}=t_{2l+1}\sum_{r=l+1}^j\cot(r\theta)\quad(l<j),
\qquad L_{jl}=0\quad(l\ge j).
\tag{49}
\]
Both finite telescoping identities behind this formula are useful. For fixed $n$, put
\[
A_{r,n}=\frac{t_rS_{r+n}}{S_{r-n-1}S_nS_{n+1}}
\quad(r\ge n+1),\qquad A_{n,n}=0.
\]
The sine identity
\[
t_{r+1}t_{r+n+1}-t_rt_{r-n}=t_{n+1}t_{2r+1}
\]
gives $A_{r+1,n}-A_{r,n}=t_{2r+1}E_{rn}$, including the initial value $A_{n+1,n}=t_{2n+1}E_{nn}$. Therefore
\[
A_{r,n}=\sum_{l=n}^{r-1}t_{2l+1}E_{ln}.
\tag{50}
\]
A second subtraction in (48) gives
\[
E_{r,n+1}-E_{r-1,n+1}
 =\frac{2\cos(r\theta)S_{r+n}}{S_{r-n-1}S_nS_{n+1}}
 =\cot(r\theta)A_{r,n}.
\tag{51}
\]
Sum from $r=n+1$ to $j$, substitute (50), and interchange the finite sums. The result is
\[
E_{j,n+1}=\sum_{l=n}^{j-1}
 t_{2l+1}\left(\sum_{r=l+1}^j\cot(r\theta)\right)E_{ln},
\]
which is $E\mathsf S=LE$. All entries retained in (49) are positive, since $r\le m<N/2$ and $2l+1<N$.

Set $\xi=4\sin^2(s\theta)$, and for an independent variable $\xi$ write
\[
w_n(\xi)=\prod_{r=1}^n(1-\xi/a_r),\qquad
K(\xi)=E\operatorname{diag}(w_n(\xi))E^{-1}.
\tag{52}
\]
For values of $\xi$ where the diagonal is invertible,
$\operatorname{diag}(w_n)Z\operatorname{diag}(w_n)^{-1}=Z+\xi\mathsf S$.
After multiplying out, polynomial continuation gives this identity at every $\xi$, and hence
$K\Lambda=(\Lambda+\xi L)K$. The lower triangular entries are consequently
\[
K_{jl}(\xi)=w_l(\xi)B_{jl}(\xi),\qquad B_{ll}=1,
\qquad
B_{jl}(\xi)=\frac{\xi}{c_l-c_j}
 \sum_{u=l}^{j-1}L_{ju}B_{ul}(\xi)\quad(j>l).
\tag{53}
\]
Every $B_{jl}$ has nonnegative coefficients. The row sums of $K$ are one because the multiplier fixes the constant polynomial. For real $0\le s<1$, every $w_l$ is positive; thus $K_s=K(4\sin^2(s\theta))$ is a positive matrix with row sums one.

For complex $s$, the same recurrence gives $|B_{jl}(\xi)|\le B_{jl}(|\xi|)$. Given $R<R'<1$, for all sufficiently large $N$ one has
$\sinh(R\theta)\le\sin(R'\theta)$. Comparison with the real parameter $R'$, together with the bounds for $|W_l(s)|/W_l(R')$ from (6), proves a uniform row-sum bound for $K_s$ on every fixed disk $|s|\le R<1$. The finitely many remaining levels are covered by compactness.

An explicit small-disk estimate will supply an inverse. For $|s|\le1/4$,
\[
|\sin(s\theta)|\le\sinh(\theta/4)\le\sin(\theta/2).
\]
For the last inequality, set $u=\theta/4\le\pi/8$; the derivative of $\sin(2u)-\sinh u$ is at least $\sqrt2-\cosh(\pi/8)>0$. Compare (53) with the real parameter $1/2$. Put $v=\sin^2(\theta/2)$ and $a=\operatorname{arsinh}\sqrt v$. The resulting row-sum multiplier is at most
\[
\prod_{r=1}^m
 \frac{1+v/\sin^2(r\theta)}{1-v/\sin^2(r\theta)}.
\tag{54}
\]
The full products from $r=1$ to $N-1$ in the numerator and denominator are
$(\sinh(Na)/(N\sqrt v))^2$ and $(1/(N\sqrt v))^2$, respectively. By reflection, (54) equals $\sinh(Na)$ at odd levels, and
$\sinh(Na)\sqrt{(1-v)/(1+v)}$ at even levels. Since $Na\le\pi/2$, both are less than four. Thus, in maximum absolute row-sum norm,
\[
\|K_s\|_\infty\le4\qquad(|s|\le1/4).
\tag{55}
\]
The matrix is an even entire function of $s$, and $K_0=I$. Cauchy's coefficient estimate in $s^2$ gives
\[
\|K_s-I\|_\infty
 \le\frac{4(4|s|)^2}{1-(4|s|)^2}.
\]
On the disk needed later this proves
\[
\|K_s-I\|_\infty\le\frac4{15},\qquad
\|K_s^{-1}\|_\infty\le\frac{15}{11},
\qquad |s|\le\frac1{16}.
\tag{56}
\]
The same bounds hold for every leading principal block. In particular, when $N$ is odd they hold for the block on the double nodes alone. Up to this point the argument concerns distinct-node values; the next section supplies all repeated-node derivatives.

## 6. Repeated-node derivatives and the full spectral norm

Let $\mathsf T_N(2\cos t)=2\cos(Nt)$. The complete algebra is
\[
\mathcal H_N=\mathbb C[z]/(\mathsf P_0(z)),\qquad
\mathsf P_0(z)=\mathsf T_N(z)+2.
\tag{57}
\]
We always use its canonical representative of degree less than $N$. Let $G_N$ be the monic polynomial with the distinct nodes $c_0,\ldots,c_m$ as its simple roots. There is a vector-space decomposition
\[
\mathcal H_N=\mathcal V_N\oplus\mathcal I_N,\qquad
\mathcal V_N=\{\deg V\le m\},\qquad
\mathcal I_N=G_N\mathbb C[z]\cap\{\deg f<N\}.
\tag{58}
\]
The first summand interpolates the node values; the second vanishes at every node and records only the repeated-node derivatives. Both are invariant under $\mathcal D_s$: they are spanned by $e_0,\ldots,e_m$ and $e_{m+1},\ldots,e_d$, respectively.

### 6.1. The trace pairing determines the derivative block

The complete Frobenius functional, in the normalization of the original closure, is
\[
\phi(f)=(-1)^dN^2[z^d]f,\qquad
\phi(e_i e_j)=\delta_{i+j,d}.
\tag{59}
\]
Here products are reduced modulo $\mathsf P_0$ before extracting the coefficient. The second formula can also be checked directly: if $i+j<d$, degree forces zero; if $i+j=d$, use $S_iS_{d-i}=N$. If $i+j\ge N$, the reflected node list $c_{d-r}=c_r$ shows that the product of the two Newton numerators contains every root of $\mathsf P_0$ with its full multiplicity, so its remainder is zero. This is the complete trace pairing used in [the positive Newton multiplication formula](actual_positive_newton_multiplication.md).

By (7) and (59), for every pair of canonical polynomials,
\[
\phi(\mathcal D_sf\,\mathcal D_sg)
 =W_d(s)\phi(fg).
\tag{60}
\]
This identity includes the nilpotent directions at the double nodes.

For $V\in\mathcal V_N$ and $I\in\mathcal I_N$, the coefficient functional has a simple residue expression:
\[
\phi(VI)=\sum_{j\in\mathcal I_{\mathrm{dbl}}}
 \alpha_j V(c_j)I'(c_j),\qquad
\alpha_j=(-1)^d4\sin^2((2j+1)\theta).
\tag{61}
\]
To verify the constant, write $\mathsf P_0=(z-c_j)^2Q_j$ at a double node. Differentiating $\mathsf T_N(2\cos t)$ twice at that node gives
\[
Q_j(c_j)=\frac12\mathsf P_0''(c_j)
 =\frac{N^2}{4\sin^2((2j+1)\theta)}.
\]
Since $I(c_j)=0$, the residue of $VI/\mathsf P_0$ is $V(c_j)I'(c_j)/Q_j(c_j)$. The simple odd-level node contributes zero. The sum of these finite residues is the coefficient of $z^{-1}$ at infinity; multiplying by $(-1)^dN^2$ gives (61). Replacing a product by its remainder changes no residue.

Let $K_s^{\mathrm{dbl}}$ be the leading value block from Section 5 on the double nodes, and let $J_s^{\mathrm{rad}}$ be the matrix of $\mathcal D_s$ on the derivative coordinates of $\mathcal I_N$. Apply (60) to $V,I$ and use (61). This gives the exact matrix identity
\[
\boxed{\displaystyle
J_s^{\mathrm{rad}}
 =W_d(s)\operatorname{diag}(\alpha_j)^{-1}
       (K_s^{\mathrm{dbl}})^{-T}\operatorname{diag}(\alpha_j).}
\tag{62}
\]
The derivative coordinates used here are independent: if $I=G_NH$, then
$H(c_j)=I'(c_j)/G_N'(c_j)$ at the double nodes determines $H$. At odd levels the extra value coordinate at $-2$ is absent from (61). The leading-block statement after (56) is exactly what makes (62) valid at that parity as well.

Every double-node angle is at least $\pi/N$ from an endpoint. Since $\sin(\pi/N)\ge2/N$,
\[
16N^{-2}\le |\alpha_j|\le4.
\tag{63}
\]
Transposition costs at most a factor $N$ in maximum row-sum norm. Equations (6), (56), and (62) therefore prove
\[
\|J_s^{\mathrm{rad}}\|_\infty
 +\|(J_s^{\mathrm{rad}})^{-1}\|_\infty
 \le CN^3,\qquad |s|\le1/16.
\tag{64}
\]
The empty derivative block is harmless. This estimate follows from the full trace pairing, not from an assumption that bounded Newton coefficients imply bounded spectral derivatives.

### 6.2. Conditioning of the decomposition

The splitting (58) costs only a polynomial factor. At even levels $N=2m_0$, its distinct-node polynomial is $G_N=\mathsf T_{m_0}$. At odd levels $N=2m_0+1$, it is
\[
G_N(z)=(z+2)\bigl(U_{m_0}(z/2)-U_{m_0-1}(z/2)\bigr),
\tag{65}
\]
where $U_j(\cos t)=\sin((j+1)t)/\sin t$. In both cases
\[
\|G_N\|_{[-2,2]}\le4,\qquad |G_N'(c_j)|\ge N/2.
\tag{66}
\]
For the odd formula, substituting $z=2\cos t$ gives
$G_N(z)=4\cos(t/2)\cos(Nt/2)$. This verifies the interior derivative bound directly; at $-2$ the derivative has magnitude $N$.

The Lagrange cardinal polynomial
\[
\ell_j(z)=\frac{G_N(z)}{(z-c_j)G_N'(c_j)}
\]
has sup norm at most $CN$ on $[-2,2]$. Indeed, the mean-value theorem bounds its numerator quotient by $\|G_N'\|_\infty$, and Markov's polynomial inequality bounds this by $CN^2$; divide by (66). Summing at most $N$ cardinal polynomials and applying Markov's inequality once more proves that the interpolant $V$ of the node values of $f$ satisfies
\[
\|V\|_{\mathrm J}\le CN^4\|f\|_{\mathrm J},\qquad
\|f-V\|_{\mathrm J}\le CN^4\|f\|_{\mathrm J}.
\tag{67}
\]
These deliberately coarse bounds suffice.

The values of $\mathcal D_sV$ are bounded by (55)–(56); its degree is still at most $m$. Apply the same interpolation bound to its output. On $I=f-V$, apply (64) to its derivative data and (67) to its input. The same reasoning works for the inverse. We obtain
\[
\boxed{\displaystyle
\|\mathcal D_sf\|_{\mathrm J}
 +\|\mathcal D_s^{-1}f\|_{\mathrm J}
 \le CN^7\|f\|_{\mathrm J},\qquad |s|\le1/16.}
\tag{68}
\]
Cauchy's formula proves polynomial estimates for every fixed $s$-derivative on smaller disks.

For completeness, the canonical polynomial sup norm is polynomially equivalent to (9). One direction is Markov's inequality. For the other, construct $V$ as above and write $I=G_NH$. Its derivative data determine $H(c_j)=I'(c_j)/G_N'(c_j)$ on the double nodes. At even levels the same cardinal-polynomial estimate applies. At odd levels use $U_{m_0}-U_{m_0-1}$ for these nodes; its sup norm and derivative bounds are polynomial, and its derivative at each zero has magnitude at least $N/8$. Interpolating $H$ therefore also has polynomial cost. Chebyshev coefficient $\ell^1$ norm and sup norm are polynomially equivalent for degree less than $N$, by the cosine coefficient formula and the triangle inequality. Thus (68) gives polynomial bounds in those norms as well, without changing the canonical representative.

### 6.3. Comparison with the complete turn

The reflection identity (7) is equivalently
\[
\mathcal R\mathcal D_s
 =H_N(s)^2\mathcal D_s^{-1}\mathcal R.
\tag{69}
\]
Insert this into (5), and apply (68) to $\mathcal Rf$. Since $H_N$, its inverse, and the six scalar phases are uniformly bounded, this proves the upper bound in (10). Apply $\mathcal D_s$ to recover $\mathcal Rf$ from the output; (68) gives the lower bound. This completes the proof of the theorem.

## 7. What the comparison does and does not propagate

The estimates retain the actual strand orientations, the full repeated-channel polynomial, and the normalized braiding carrier. They compare turns of the same canonical input polynomial. They do not replace multiplication in a moving same-color algebra by complete multiplication: the relation is
\[
\mathsf T_N(z)+2\cos(2\pi s)=0,
\]
and the additional high-index multiplication sectors described in [the moving Newton multiplication calculation](actual_main_meridian_newton_multiplication.md) remain present. A bound for a fixed finite product in a signed polynomial norm is also different from a bound for an entire contraction at its geometric exponential rate.

There is a concrete limitation to what node localization alone can imply. Take even $N\ge4$, put $b=N/2-1$, and let $I_N\in\mathcal I_N$ be the unique radical element with
\[
I_N'(c_b)=1,\qquad I_N'(c_j)=0\ (j\ne b),\qquad
I_N(c_j)=0\ \text{for every }j.
\tag{70}
\]
Its spectral-jet norm is one and its data are supported at the node nearest $-2$. This does not assert that its canonical polynomial satisfies the global complex-strip envelope required of a physical source packet.

Differentiate (53) and (62), using
$4\sin^2(s\theta)=4\theta^2s^2+O(s^4)$. Since $\alpha_b=\alpha_0$, the offdiagonal second derivative is
\[
\left.\partial_s^2(\mathcal D_sI_N)'(c_0)\right|_{s=0}
 =-8\theta^2\frac{L_{b0}}{c_0-c_b}.
\tag{71}
\]
The derivative of $W_d$ contributes no offdiagonal term. Here
\[
L_{b0}=2\sin\theta\sum_{r=1}^b\cot(r\theta)\asymp\log N,
\qquad c_0-c_b=4\cos\theta\asymp1.
\tag{72}
\]
The first comparison follows by a harmonic-sum comparison for $r\le N/4$, with the remaining terms bounded by the same sum. Thus (71) has magnitude of order $(\log N)/N^2$, even though $c_0$ is near $+2$. A uniform analytic estimate that propagated every endpoint-supported set of node jets to exponentially small jets at the opposite end would contradict Cauchy's derivative estimate applied to (71). Polynomial full-norm stability is therefore proved, but automatic Gaussian propagation from such node data is false. The test element is an algebra element, not a claimed tangle or knot.

The [whole-source growth theorem](actual_main_meridian_source_bounds.md) combines this turn formula with the actual crossing-circle operators and a signed whole-junction comparison. For strict trees whose bare product junctions are separated by junctions carrying an original circle operator, it gives an exact supremum-volume limit on \(|s|\le R<1\), at both parities, at the original augmented volume. Its proof creates angular localization from the actual coefficient bounds; it does not infer it from the arbitrary localized node data above. The [component extension](actual_main_meridian_component_extension.md) handles some adjacent bare junctions, and the [filled-meridian theorem](actual_main_meridian_filled_volume.md) adds the joint Fourier and geometric arguments giving the normalized profile and uniform filled-knot volume for that class. No classical meridian factor is identified by these results.

## Appendix A. The moving Newton coordinates

The fixed-frame result can also be expressed in the moving input basis $e_n^s$. This records the additional entries that are hidden by the simpler fixed-frame reversal. Define
\[
b_0(s)=1,\qquad
b_j(s)=\prod_{r=0}^{j-1}\frac{\sin((s-r)\theta)}{\sin((r+1)\theta)}
\quad(j\ge1),\qquad b_j(s)=0\quad(j<0).
\tag{A1}
\]
For the same-color turn (17),
\[
\widehat{\mathcal T}_s(e_n^s)
 =\sum_{k=0}^dT_{kn}(s)e_k,\qquad
T_{kn}(s)=q^{-s^2/2}\frac{P_n(s)}{P_k(s)}b_{k+n-d}(s).
\tag{A2}
\]
In particular it vanishes for $k+n<d$; the entries $k+n>d$ are retained.

Here is a finite recurrence proof, independent of a summation formula. Multiplication in the moving input Newton basis has diagonal $c_n(s)$ and subdiagonal $-4\sin^2((n+1)\theta)$. Equation (34) implies that the output columns satisfy
\[
T\mathbf e_0=\frac{q^{-s^2/2}}{H_N(s)}\mathbf e_d,
\qquad
T\mathbf e_{n+1}
 =\frac{c_n(s)I-\mathsf L_s}{4\sin^2((n+1)\theta)}T\mathbf e_n.
\tag{A3}
\]
For an interior entry, set $j=k+n-d$. Substituting (A2), and using
$b_{j+1}/b_j=[s-j]/[j+1]$ and $P_{n+1}/P_n=[n+1-s]/[n+1]$, reduces (A3) to
\[
\sin((n+1)\theta)\sin((n+1-s)\theta)
 -\sin((k+1)\theta)\sin((k+1+s)\theta)
 =-\sin((j+1)\theta)\sin((n-k-s)\theta).
\tag{A4}
\]
Product-to-sum proves this because $n+k+2=N+j+1$. Clear the factors before taking a zero of $b_j$; the identity then also handles $j=-1$. For $j<-1$ every entry is zero. At $k=d$ the recurrence is instead the direct identity
\[
c_n(s)-c_d=4\sin((n+1-s)\theta)\sin((s-n)\theta).
\]
The bottom-left entry in (29) does not act on the first $d$ columns, whose zeroth coordinate is zero, but remains in the full multiplication intertwiner. The initial column in (A3) agrees with (A2), so induction proves all columns.

If $\mathsf U_s$ is the lower triangular Toeplitz matrix with entries
$(\mathsf U_s)_{kt}=b_{k-t}(s)$, the factorization is
\[
T=q^{-s^2/2}\mathsf D_s^{-1}\mathsf U_sJ\mathsf D_s,
\qquad \mathsf U_s^{-1}=\mathsf U_{-s}.
\tag{A5}
\]
For the inverse identity, write
\[
b_j(s)=(-q^{s+1})^j\frac{(Q^{-s};Q)_j}{(Q;Q)_j}.
\]
Here $(a;Q)_j=\prod_{r=0}^{j-1}(1-aQ^r)$. Work with the finite power series
$F_s(z)=\sum_{j=0}^{N-1}b_j(s)z^j$ modulo $z^N$. The ratio of two consecutive coefficients gives
\[
(1+q^{s+1}z)F_s(z)
 =(1+q^{1-s}z)F_s(Qz)\pmod{z^N}.
\]
Multiply this identity by its sign-reversed version and cancel the two factors with constant term one. The product $F_s(z)F_{-s}(z)$ is unchanged by $z\mapsto Qz$ modulo $z^N$. Since $1-Q^r\ne0$ for $1\le r<N$, every nonconstant coefficient in that range vanishes. Its constant term is one, proving (A5) by a finite coefficient identity.

The moving-basis connection is therefore compatible with (5), but it is not an identification of different physical Casimir realizations. The cup calculation (31)–(34) is what supplies that identification for the actual turn.

## Appendix B. Finite reproduction of the formulas

The [reproduction script](../experiments/audit_main_meridian_turn_comparison.py) constructs the full physical modules, coproduct Casimir, evaluation and coevaluation matrices, and checked braid. It computes the turn directly from those matrices and the full inverse $r_0^{-1}$, rather than from the recurrence (A3). It also checks the Frobenius pairing, positive shift kernel, and derivative block by exact cyclotomic arithmetic at small levels. The [recorded results](../experiments/main_meridian_turn_comparison_results.json) specify the levels, parameters, precision, and errors.

These finite calculations test the indexing, orientation, and scalar conventions independently of the matrix recurrence. The uniform bounds in Sections 4–6 follow from the proofs above; they are not extrapolations from the finite calculation.
