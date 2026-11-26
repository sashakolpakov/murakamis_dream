# Coherent full-normal traces of physical row products

Private written proof, 17 November 2026.

The positive coefficient contour for a product of physical value
rows also controls its original boundary normals. The source-exact
Jacobi derivative replaces each normal by a polynomial cofactor
and the Ward endpoint coupon. The coupon has a cut, which is
retained below. Its jump is polynomial, and the entire uncharged
cut lies strictly below the positive coefficient saddle.

This proves a polynomial relative upper bound for every mixed
first normal, uniformly over all physical rows with a fixed
support margin. In a strict bulk degree chart the leading mixed
normal is nonzero. A single holomorphic scalar packet then
approximates all those physical jets with exponential accuracy.
No charged closing, arbitrary-height continuation, or complete
network lower bound follows from this local packet.

## 1. Original source and statements

Let \(N\ge3\), \(D=N-1\), \(J=\lfloor D/2\rfloor\), and
\[
 \theta=\pi/N,\qquad c_j=2\cos((2j+1)\theta),\qquad
 P_N(C)=2T_N(C/2)+2,\qquad \eta=(-1)^D.
 \tag{1}
\]
The \(N\) indices of the roots of \(P_N\) include their
multiplicities. The original trace is
\[
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
Put
\[
 F_j(C)=K_N(c_j,C),\qquad
 G_j(C)=\left.\partial_wK_N(w,C)\right|_{w=c_j}.
 \tag{3}
\]
The normal \(G_j\) is prescribed only at a double physical
node. At the odd simple node \(j=J\), only the value is used.

Fix \(m\ge3\), \(\varepsilon>0\), and physical indices satisfying
\[
                  k=\sum_{i=1}^m j_i-D\ge\varepsilon N.
 \tag{4}
\]
Write
\[
 \Gamma_{\mathbf j}=\phi_N\Bigl(\prod_iF_{j_i}\Bigr)>0,\qquad
 \Gamma_{\mathbf j,I}
 =\phi_N\Bigl(\prod_{i\in I}G_{j_i}
                         \prod_{i\notin I}F_{j_i}\Bigr),
 \tag{5}
\]
where \(I\) contains only double-node indices.
The positive coefficient theorem supplies its actual saddle
\(\rho=\rho_{\mathbf j,N}\), with
\[
 0<a\le\rho\le b<1/4,\qquad V_N\asymp N.
 \tag{6}
\]
All constants in (6) depend only on \(m,\varepsilon\).
Set
\[
 R=\rho^{-1},\qquad C_-=c_0-R,\qquad C_+=c_0+R,\qquad
 M_{\mathbf j}(R)=
       \frac{\prod_iF_{j_i}(C_-)}{|P_N(C_-)|}.
 \tag{7}
\]
For large \(N\), \(C_-<-2\), with a fixed margin.
The exact coefficient normalization gives
\[
 \Gamma_{\mathbf j}
   =\frac{N^2R\,M_{\mathbf j}(R)}
                   {\sqrt{2\pi V_N}}\bigl(1+O(N^{-1})\bigr).
 \tag{8}
\]

**Theorem 1 (all physical rows).** There are constants \(B,C\),
depending only on \(m,\varepsilon\), such that
\[
                  |\Gamma_{\mathbf j,I}|
                         \le C N^B\Gamma_{\mathbf j}.
 \tag{9}
\]
This is uniform in every physical row, both parities, and
every allowed subset \(I\). It includes \(j=0\), even last
normals, and odd simple values.

For the leading coefficient, define on \(0<x<1/2,\ C<2\)
\[
 g(x,C)=-
 \frac{2\operatorname{arsinh}
          \bigl(\tfrac12\sqrt{2-C}\cot(\pi x)\bigr)}
                {4\pi\sin(2\pi x)}.
 \tag{10}
\]
The square root and inverse hyperbolic sine have their
positive real branches here.

**Theorem 2 (bulk normal coefficients).** In addition to (4),
suppose that \(j_i/N\) for \(i\in I\) stays in a fixed compact
subinterval of \((0,1/2)\). Then
\[
 \frac{\Gamma_{\mathbf j,I}}{\Gamma_{\mathbf j}}
 =N^{|I|}
   \left\{\prod_{i\in I}g(j_i/N,C_-)
                    +O\!\left(\frac{\log N}{N}\right)\right\}.
 \tag{11}
\]
The error is uniform; the unselected value rows may still
approach either endpoint or the fold. Each selected factor
in (10) is negative and bounded away from zero. Thus (11)
has a nonzero leading coefficient, with sign \((-1)^{|I|}\).

Here is the scalar assertion needed to distinguish coherent
normal data from separate normal estimates. Let
\[
 \mathcal B\Subset
 \{(x_1,\ldots,x_m):0<x_i<1/2,\ \sum_i x_i>1\}
 \tag{12}
\]
be a real compact set, and let
\[
 \boldsymbol\Gamma_N(w_1,\ldots,w_m)
       =\phi_N\Bigl(\prod_iK_N(w_i,C)\Bigr).
 \tag{13}
\]

**Theorem 3 (one scalar packet on each bulk chart).**
A finite cover of \(\mathcal B\) by real product neighborhoods
has the following property. On a fixed complex neighborhood
of each such product there is a holomorphic scalar
\(\mathcal W_N(\mathbf x)\) and constants \(B,\gamma>0\)
such that, at every physical tuple in that product,
\[
 \left|
 \left[\prod_{i\in I}
       \frac{1}{C_N'(x_i)}\partial_{x_i}\right]
       \mathcal W_N(\mathbf x)\Big|_{\mathbf x=\mathbf j/N}
            -\Gamma_{\mathbf j,I}\right|
       \le C N^B e^{-\gamma N}\Gamma_{\mathbf j},
 \quad C_N(x)=2\cos(2\pi x+\theta).
 \tag{14}
\]
This includes \(I=\varnothing\) and all \(2^m\) mixed first
jets. Equivalently \(\mathcal W_N\), expressed in the local
external spectral coordinates \(w_i=C_N(x_i)\), is a single
scalar approximation to (13) and those derivatives.

The physical error exponent in Theorem 3 comes only from
the omitted coefficient-circle arc and the paid cut, minus
the explicitly bounded reference-radius loss. The analytic
normal-connection rate sets the available thin complex
neighborhood, but does not enter that physical error exponent.
The charts are strict bulk charts. The theorem does not
prescribe fold normals, compare charts on a tall complex
continuation, or compare its gaps with a charged-closing loss.

## 2. The exact normal representative and its cut

Use the actual common-shift Jacobi determinant, with \(c_0\)
held fixed:
\[
 F_j^\epsilon(C)=
 \frac{\det(\mathcal J_j(\epsilon)-CI)}
                  {\prod_{r<j}A(r+\epsilon)},\qquad
 R_j(C)=\left.\partial_\epsilon F_j^\epsilon(C)\right|_0.
 \tag{15}
\]
Set \(R_0=0\). Its spectral eigenvalues exceed \(c_0\);
write \(r_{j,b}=\lambda_{j,b}-c_0>0\). In particular
\[
               F_j(c_0-z)=\prod_{b=1}^j(1+z/r_{j,b}).
 \tag{16}
\]
For \(j\ge1\) in the double-node range, the pinned source gives
\[
 \begin{split}
 c'(j)G_j(C)={}&c'(0)F_j(C)Q_0(C)+R_j(C)\\
 &+\frac{c'(0)P_N(C)}{N^2s_1^2}
                F_j(C)[(\mathcal J_j-CI)^{-1}]_{00},
 \end{split}
 \tag{17}
\]
where \(Q_0=G_0\), \(s_1=2\sin\theta\), and
\[
 c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{18}
\]
At \(j=0\), the endpoint is simply \(G_0=Q_0\).
The last factor in (17), after multiplication by \(F_j\),
is a polynomial cofactor. Thus there are no genuine
Jacobi-resolvent poles in this expression.

Let \(\widetilde Q_N\) be the actual even Ward representative
of \(Q_0\), descended to
\(\Omega=\mathbb C\setminus[2,\infty)\). Define
\[
 \widehat G_j(C)=
  \frac{c'(0)F_j(C)\widetilde Q_N(C)+R_j(C)}{c'(j)}.
 \tag{19}
\]
For \(j=0\) this is \(\widetilde Q_N\).
It has the value and required first inner-\(C\) normal of
the original \(G_j\) at every physical inner node.
Consequently products in (5) may use (19) inside their
original trace, with the complete product rule. This uses
the full physical ideal, including the simple odd node;
it is not an equality between free off-grid polynomials.

The uniform source bounds are
\[
 |c'(j)|^{-1}\le C N^2,\qquad
 \|\mathcal J_j'\|\le6\pi N^3,\qquad
 |A'/A|\le4\pi.
 \tag{20}
\]
On every fixed-height physical angular rectangle,
\[
                    |\widetilde Q_N|\le C N^2(1+\log N).
 \tag{21}
\]
The compact spectral circles and their two banks below
are contained in such rectangles on the original branch.

The jump in (21) is explicit. Write
\(\sigma=(-1)^N=-\eta\) and
\(\ell_N(t)=D/2-t/(2\theta)\). The Ward function \(V_N\)
satisfies
\[
 \widetilde Q_N(-2\cos t)
       =\frac{\eta V_N(t)+c_0}{4\sin^2\theta},\qquad
 V_N(t+2\pi)-V_N(t)
       =-2\sigma N\sin\theta\cot(\pi\ell_N(t)).
 \tag{22}
\]
For \(C=2\cosh h\), \(h\ge0\), the upper spectral bank is
\(t_+=\pi+ih\), and the lower bank may be written
\(t_-=-\pi+ih\), using the evenness of \(V_N\).
Since
\(\ell_N(t_-)=N-\tfrac12-iNh/(2\pi)\), (22) gives
\[
 \boxed{\quad
 \widetilde Q_{N,+}(2\cosh h)
       -\widetilde Q_{N,-}(2\cosh h)
       =\frac{iN}{2\sin\theta}\tanh(Nh/2).
 \quad}
 \tag{23}
\]
This sign uses upper minus lower bank. Both the jump and
each bank have polynomial size. At \(C=2\) the two banks
meet and the jump vanishes.

Let
\[
 \mathcal P_I(C)=
       \prod_{i\in I}\widehat G_{j_i}(C)
                         \prod_{i\notin I}F_{j_i}(C).
 \tag{24}
\]
Start from small contours around the physical spectrum,
where (19) has the exact source data, and enlarge them to
the circle \(|C-c_0|=R\), cut at its right intersection.
Cauchy's theorem gives the exact identity
\[
 \Gamma_{\mathbf j,I}=\frac{\eta N^2}{2\pi i}
 \left\{
   \int_{\mathcal C_R}\frac{\mathcal P_I(C)}{P_N(C)}\,dC
   +\int_2^{C_+}
           \frac{\mathcal P_{I,+}(C)-\mathcal P_{I,-}(C)}
                {P_N(C)}\,dC
 \right\}.
 \tag{25}
\]
The outer circle is counterclockwise with its original
slit branches. The upper cut bank runs from \(2\) to
\(C_+\), and the lower bank returns. The shrinking cap
at \(2\) contributes zero: the numerator is bounded
there and \(P_N(2)=4\). No cut term has been deleted.

## 3. Cofactor omissions preserve the circle gap

Diagonalizing the real symmetric matrix
\(\mathcal J_j-c_0I\) gives
\[
 R_j(c_0-z)=
 \frac{\displaystyle\sum_b d_{j,b}
                \prod_{a\ne b}(r_{j,a}+z)}
      {\prod_{r<j}A(r)}
 -\left(\sum_{r<j}A'(r)/A(r)\right)F_j(c_0-z),
 \qquad |d_{j,b}|\le\|\mathcal J_j'\|.
 \tag{26}
\]
This formula is valid also at repeated eigenvalues: choose
any orthonormal eigenbasis and take the diagonal entries of
\(\mathcal J_j'\). It is a polynomial identity.

On \(z=Re^{i\vartheta}\), division by \(F_j(C_-)\)
turns each full factor into
\((r+Re^{i\vartheta})/(r+R)\), of modulus at most one.
Omission of one factor costs at most \((r+R)^{-1}\le R^{-1}\).
The sum in (26), (20), and the Ward bound (21) show that
every fixed normal product has only a polynomial loss.
This argument does not require an upper bound on a
Jacobi eigenvalue.

More importantly, the denominator alone gives a strict gap.
Put \(d_a=c_0-c_a\ge0\). A fixed positive fraction of the
\(d_a\)'s lie in \([1,2]\), and \(R^{-1}\in[a,b]\).
Consequently
\[
 \frac{|P_N(C_-)|}{|P_N(c_0-Re^{i\vartheta})|}
 =\prod_a
       \frac{1-\rho d_a}{|1-\rho d_ae^{-i\vartheta}|}
 \le \exp\{-cN\sin^2(\vartheta/2)\}.
 \tag{27}
\]
Indeed each of those geometric factors equals
\(\{1+4u(1-u)^{-2}\sin^2(\vartheta/2)\}^{-1/2}\),
with \(u=\rho d_a\) bounded away from zero and one.
Omitting numerator factors leaves all of (27) available.
Thus
\[
 \left|\frac{\mathcal P_I(c_0-Re^{i\vartheta})}
                       {P_N(c_0-Re^{i\vartheta})}\right|
 \le C N^B M_{\mathbf j}(R)
                   e^{-cN\sin^2(\vartheta/2)}.
 \tag{28}
\]
This includes the two one-sided limits at the cut.
The circle integral is at most
\(C N^{B-1/2}M_{\mathbf j}(R)\).

## 4. The whole uncharged cut has a strict gap

The original slit profile is
\[
 \Psi_x(C)=
 2\int_0^x\operatorname{arsinh}
          \bigl(\tfrac12\sqrt{2-C}\cot(\pi s)\bigr)\,ds,
                   \qquad 0\le x\le1/2.
 \tag{29}
\]
The all-row source theorem gives
\[
 N^{-1}\log|F_j(C)|=\Re\Psi_{j/N}(C)+o(1)
 \tag{30}
\]
uniformly over all physical rows on each compact slit set.
Only this uniform \(o(1)\) is used on the slit.
On half-plane compacts the stronger error is
\(O(\log N/N)\).

For \(C=2\cosh h\) on the upper bank, define
\[
 B_x(h)=\Re\Psi_x(2\cosh h+i0)
  =2\int_0^{\min(x,\pi^{-1}\arctan(\sinh(h/2)))}
       \operatorname{arcosh}
                \bigl(\sinh(h/2)\cot(\pi s)\bigr)\,ds.
 \tag{31}
\]
The real part in (29) converges continuously to (31),
uniformly in \(x\in[0,1/2]\) and bounded \(h\).
To see this directly, split the integral at a small
positive \(s\); away from zero continuity is uniform,
and near zero a uniform bound \(C(1+|\log s|)\)
has an arbitrarily small integral. This also treats
the moving threshold of the inverse hyperbolic cosine.

For \(h>0\), differentiating (31) has no boundary term
because its integrand vanishes at the moving endpoint.
The substitution \(v=\sin(\pi s)\) gives
\[
 B_x'(h)=\frac1\pi
     \arcsin\!\left(\min\{\coth(h/2)\sin(\pi x),1\}\right)
                       \ge x.
 \tag{32}
\]
In particular \(B_{1/2}(h)=h/2\).
For \(x_i=j_i/N\), set
\[
                 \mathcal A_{\mathbf x}(h)
                    =\sum_iB_{x_i}(h)-h.
 \tag{33}
\]
By (4), for large \(N\),
\[
             \mathcal A_{\mathbf x}'(h)
                    \ge\sum_i x_i-1\ge\varepsilon/2.
 \tag{34}
\]
Thus the cut action is increasing. This statement concerns
the uncharged product; it has no extra filling factor.

Here is a rigorous bound on the finite source along the
cut, including zeros of determinants. For real \(C\),
all roots of \(F_j\) are real, so for fixed \(\delta>0\)
\[
 |F_j(C)|\le|F_j(C+i\delta)|.
 \tag{35}
\]
Every omitted-factor term in (26) satisfies
\[
 \left|\prod_{a\ne b}(\lambda_{j,a}-C)\right|
 \le\delta^{-1}
           \prod_a|\lambda_{j,a}-C-i\delta|.
 \tag{36}
\]
Equations (20)--(23), (26), and (36) therefore imply,
uniformly on the whole finite cut,
\[
 |\mathcal P_{I,+}(C)-\mathcal P_{I,-}(C)|
       \le C_\delta N^B\prod_i|F_{j_i}(C+i\delta)|.
 \tag{37}
\]
For \(I=\varnothing\) the left side is zero.
Fix \(\delta\) first, use (30), then use the uniform
continuity following (31). Since
\[
                  P_N(2\cosh h)
                    =e^{Nh}(1+e^{-Nh})^2\ge e^{Nh},
 \tag{38}
\]
for any fixed tolerance \(\tau>0\) we obtain
\[
 \left|\frac{\mathcal P_{I,+}(2\cosh h)
                     -\mathcal P_{I,-}(2\cosh h)}
                    {P_N(2\cosh h)}\right|
 \le C_\tau N^B
             e^{N\{\mathcal A_{\mathbf x}(h)+\tau\}},
             \quad 0\le h\le h_{+,N},
 \tag{39}
\]
where \(h_{+,N}=\operatorname{arcosh}(C_+/2)\).
No estimate by the inverse of \(F_j(C)\) on the cut
has been used.

It remains to compare its endpoint with the actual saddle.
Put \(h_{-,N}=\operatorname{arcosh}(-C_-/2)\).
The allowed \(R\)'s form a compact subinterval of \((4,\infty)\);
since \(c_0\to2\), there is a fixed \(\Delta>0\) such that
\[
                       h_{+,N}-h_{-,N}\ge\Delta.
 \tag{40}
\]
The numerator cannot erase this denominator gap.
Indeed, with \(R_\delta=\sqrt{R^2+\delta^2}\), (16) gives
\[
 |F_j(C_++i\delta)|
       \le F_j(c_0-R_\delta)
       \le F_j(C_-)(R_\delta/R)^j.
 \tag{41}
\]
The last exponent costs \(O(N\delta^2)\), uniformly in all
indices. Apply (30) at \(C_++i\delta\), then take the
boundary limit using (31). It follows, uniformly over the
tuples and allowed radii, that
\[
 \sum_i B_{x_i}(h_{+,N})
       \le N^{-1}\log\prod_iF_{j_i}(C_-)+o(1).
 \tag{42}
\]
For full precision in (42), any desired positive tolerance
is first obtained by fixing a sufficiently small \(\delta\);
the remaining \(o(1)\) is then supplied by (30).
This is sufficient with the fixed gap in (40).
Also
\[
       \log|P_N(C_-)|=Nh_{-,N}+O(1)
 \tag{43}
\]
uniformly, at both parities. Equations (34), (40)--(43),
with tolerances smaller than \(\Delta/4\), prove
\[
 \left|\int_2^{C_+}
     \frac{\mathcal P_{I,+}-\mathcal P_{I,-}}{P_N}\,dC\right|
        \le C N^B M_{\mathbf j}(R)e^{-\gamma_0N}
 \tag{44}
\]
for a fixed \(\gamma_0>0\).
The finite cut length is uniformly bounded. The argument
includes \(h=0\), every root threshold, and every physical
row. Combining (25), (28), (44), and (8) proves Theorem 1.

## 5. The leading bulk normal insertion

On a fixed bulk degree interval and a buffered compact
negative spectral neighborhood containing all \(C_-\), the
pinned slit-normal connection gives one holomorphic unit
\(A_N(x,C)\) with
\[
 \begin{split}
 A_N(j/N,C)&=F_j(C)(1+O(e^{-\kappa N})),\\
 \partial_xA_N(j/N,C)
      -C_N'(j/N)\widehat G_j(C)
                         &=F_j(C)O(e^{-\kappa N}),\\
 \log A_N(x,C)-N\Psi_x(C)&=O(\log N).
 \end{split}
 \tag{45}
\]
The construction uses an actual physical anchor.
These bounds hold on larger fixed domains before
differentiation. Cauchy's formula in \(x\) and \(C\) gives
\[
 N^{-1}\frac{\widehat G_j(C)}{F_j(C)}
       =g(j/N,C)+O(\log N/N),
 \tag{46}
\]
with all fixed \(C\)-derivatives. Here
\(C_N'(x)=-4\pi\sin(2\pi x+\theta)\); replacing it by
\(-4\pi\sin(2\pi x)\) costs \(O(N^{-1})\).
This proves precisely (10), including its sign.

Restrict (25) to a fixed small arc about \(\vartheta=0\).
The rest of the circle and the entire cut have exponential
gaps by (28),(44). On that arc the normalized insertion
\[
 a_N(C)=N^{-|I|}
                  \prod_{i\in I}\frac{\widehat G_{j_i}(C)}
                                             {F_{j_i}(C)}
 \tag{47}
\]
is holomorphic with uniformly bounded fixed derivatives.
There are no roots of \(F_j\) in this negative neighborhood.

The scalar coefficient Fourier integral from the positive
source has zero linear term at \(\rho\), variance \(V_N\),
and cumulants of every fixed order \(O(N)\). Its modulus
has (27). Multiplication by a holomorphic insertion with
bounded first two derivatives gives
\[
 \frac{\text{inserted circle integral}}
      {\text{value circle integral}}
                  =a_N(C_-)+O(N^{-1}).
 \tag{48}
\]
For completeness, on \(|\vartheta|\le N^{-2/5}\) expand
the insertion through its linear term and the centered
characteristic function through its cubic term. Each
single odd term integrates to zero on the symmetric
interval. The remaining errors are bounded by
\(C(V_N^{-1}+N V_N^{-2}+N^2V_N^{-3})=O(N^{-1})\).
Outside that interval (27) is negligible. The analytic
map \(C=c_0-Re^{i\vartheta}\) has uniformly bounded
derivatives, so these estimates apply to (47).
The polynomial global normal bound makes the discarded
arc and cut negligible also after normalization.
Equations (46)--(48) prove (11).

## 6. An exponentially accurate common scalar packet

We use the exact scalar correction from Section 6 of the
pinned slit-normal connection. On a sufficiently thin fixed
degree neighborhood, it gives a holomorphic function
\(\mathfrak F_N(x,C)\) satisfying, identically in \(C\)
on the buffered negative spectral domain,
\[
 \mathfrak F_N(j/N,C)=F_j(C),\qquad
 \partial_x\mathfrak F_N(j/N,C)
                         =C_N'(j/N)\widehat G_j(C).
 \tag{48a}
\]
This is the finite \(\operatorname{sinc}^2\) correction of
the two normalized errors in (45); its scalar construction
preserves both jets at every other degree node as well.
It obeys a polynomial normalized own-profile bound on
the present half-plane compact. The exponential rate
\(\kappa\) in (45) limits the thickness allowed for that
bound. It does not create an error in (48a).

We give a uniform fixed-chart contour rather than letting
it depend nonholomorphically on the external variables.
Choose a reference real tuple in (12), a nearby
physical tuple at each \(N\), and its exact saddle
\(\rho_{0,N}\). Write \(R_{0,N}=\rho_{0,N}^{-1}\).
Take one small symmetric arc
\[
 \gamma_{0,N}:\quad
       C=c_0-R_{0,N}e^{i\vartheta},\qquad
                       |\vartheta|\le\vartheta_0,
 \tag{49}
\]
oriented counterclockwise as part of that circle.
Choose \(\vartheta_0>0\) small enough that all these arcs
and fixed neighborhoods lie in the negative spectral
domain used in (45). Define
\[
 \mathcal W_N(\mathbf x)=
       \frac{\eta N^2}{2\pi i}
         \int_{\gamma_{0,N}}
             \frac{\prod_i\mathfrak F_N(x_i,C)}{P_N(C)}\,dC.
 \tag{50}
\]
This is one jointly holomorphic scalar. The external
coordinate change \(w_i=C_N(x_i)\) is univalent on
sufficiently small bulk neighborhoods.

We verify that the same arc works for an entire fixed
real product neighborhood. Jacobi matrices of successive
sizes are nested principal matrices. Interlacing and
the increasing function
\(r\mapsto\rho r/(1+\rho r)\in[0,1]\) show that increasing
one \(j_i\) by one changes its Bernoulli mean by a number
in \([0,1]\). The target integer \(k\) changes by one.
On a slightly enlarged compact \(\rho\)-interval,
\(\mu_N'(\rho)\asymp N\). Therefore the exact saddle
satisfies the uniform lattice Lipschitz estimate
\[
 |\rho_{\mathbf j,N}-\rho_{\mathbf j',N}|
       \le \frac{C}{N}\sum_i|j_i-j_i'|.
 \tag{51}
\]
All comparisons stay within the fixed support margin.

For the source-specific coefficient function \(H\), set
\(\mathcal F(\rho)=\log H(\rho)-k\log\rho\).
At its saddle \(\mathcal F'=0\), and
\(\mathcal F''=O(N)\) on the relevant compact interval
(use the mean and variance formulas). Thus, if
\(|\mathbf j/N-\mathbf x^0|\le\delta\),
\[
 0\le\mathcal F(\rho_{0,N})
                   -\mathcal F(\rho_{\mathbf j,N})
                   \le C N\delta^2+O(N^{-1}).
 \tag{52}
\]
Equivalently the value mass \(R M_{\mathbf j}(R)\) at
the reference radius is at most
\(e^{CN\delta^2+O(1)}\) times its mass at the actual saddle.
The elementary identity behind this equivalence is
\(R M_{\mathbf j}(R)=a_{\mathbf j}H(\rho)\rho^{-k}\).

The bounds (28),(44) apply to any radius in the enlarged
compact interval, regardless of whether it is the current
tuple's saddle. At the reference radius let
\[
 g_{\rm arc}=c\sin^2(\vartheta_0/2),\qquad
 g_{\rm cut}=\gamma_0,
 \tag{53}
\]
where \(c\) is the uniform constant in (28) and
\(\gamma_0\) is the cut gap in (44).
Choose \(\delta>0\) after these constants and after
\(\vartheta_0\), so that the loss \(C\delta^2\) in (52)
is smaller than half of \(\min(g_{\rm arc},g_{\rm cut})\).

At a physical tuple, differentiating (50) in any subset
of its distinct external variables replaces the
corresponding \(\mathfrak F_N\)'s by
\((C_N')^{-1}\partial_x\mathfrak F_N\).
Equation (48a) identifies the resulting integrand
exactly with (24) on the retained arc. This holds
simultaneously for every mixed subset \(I\).
Thus the physical comparison error consists precisely
of the omitted circle arc and the entire cut in (25).
They are exponentially small by the preceding paragraph.
Finally (8) compares the mass to \(\Gamma_{\mathbf j}\).
Any fixed positive
\[
          \gamma<
          \min(g_{\rm arc},g_{\rm cut})-C\delta^2
 \tag{54}
\]
is allowed after adjusting the polynomial prefactor.
This proves (14) for every subset \(I\).
A finite cover of the compact set in (12) completes
Theorem 3.

The argument constructs the scalar packet with exact
source-compatible arc jets, rather than assigning
independent normal functions to value estimates.
The rate \(\kappa\) from (45) enters only the available
complex strip and its normalized holomorphic bound;
it is absent from (54). No off-grid approximation to
the canonical polynomial (13), or comparison of (54)
with a subsequent charged-closing loss, is asserted.

## 7. Scope and complete direct sources

The all-row estimate (9) controls the original mixed
boundary normals before any further signed observation.
The cut in (25) is part of the proof, not a discarded
ideal multiple. A crossing representative has an
exponentially large jump on this same cut; its additional
action is not covered by (34) or (44).

The packet (50) covers only its stated bulk physical
tuples. It does not replace the whole original grid,
cancel exterior currents, or provide a lower bound after
an arbitrary crossing. Its common mixed jets remove a
local normal-compatibility ambiguity, with an explicit
source-preserving contour and retained correction.

The complete direct texts and their used implications
were read at these pins:

* [Positive coefficient saddle for physical products](research_physical_products_positive_coefficient_saddle.md),
  SHA256 e82fea1f786383a1cfe4529573805adf5fc75a77e433e38ea609024bdeed7824:
  exact positive coefficient, all-row compact saddle,
  denominator characteristic gap, and local central limit.
* [Physical Jacobi charge boundary](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  actual determinant, common-shift cofactor identity,
  uniform row bounds, and full-inner-trace normal substitution.
* [Odd Ward logarithmic factorial](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_odd_ward_logarithmic_factorial.md),
  SHA256 63ae4693846f00a9b843b98b423959964a8ccb3a72dc8ee0fc1ac36b69f3d4b8:
  even full-jet endpoint representative, physical-rectangle
  bound, and exact angular monodromy.
* [Physical-row slit-plane bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b:
  uniform all-row profile, its original normalization,
  and the stronger half-plane logarithmic remainder.
* [Actual slit normal connection](research_physical_row_slit_normal_connection.md),
  SHA256 a5084adb4ff25cb08020e5f9485bd1aaea5b49468c6ab0af311ebc1c0c504d99:
  one actually anchored scalar mode with exponential value
  and independent-normal agreement, and its exact scalar
  full-jet correction on thin bulk degree charts.

Only written mathematics, text reads and metadata hashes
were used. No mathematical programs, tests, numerical
evaluations, or builds were run. Frozen notes and public
manuscripts are unchanged.
