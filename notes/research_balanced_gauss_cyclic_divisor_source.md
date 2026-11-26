# The actual balanced Gauss source as a cyclic divisor contraction

Private written proof, 18 November 2026.

The finite balanced Gauss polynomial in the actual opposite source is
an exact Fourier interpolation of a full square of shifted factorial
ratios. Those ratios are the multiplication coefficients of one finite
cyclic algebra. Its closed residue contour retains all poles, becomes
nilpotent at completeness, and has an explicit first-normal carry with
coefficient \(2N\). The construction descends polynomially to the actual
commuting Cartan and Casimir, including their Jordan data.

This is an exact source adapter. It does not assert an asymptotic for
the reconstructed coherent kernel, remove its exterior coupons, or
select a geometric contribution. Complete direct G supplies the actual
Gauss factor and F supplies the proved meridian frame bounds. All
Fourier, algebra, residue, and normal calculations for the adapter are
proved here.

Finite-flat Fermat/socle residue constructions already occur in
[the earlier charged-source note](actual_charged_socle_and_fermat_source.md).
That is coverage, not a proof premise here. The present identification
is for the literal balanced Gauss factor, its calibrated functional,
and its quantitative upper-carry sector.

## 1. The actual operator to be transported

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
The quantum root is fixed. Put
\[
 c=M^{-2}Q,\qquad f_n=(Q;Q)_n,\qquad
 g_n(c)=(c;Q)_n,\qquad \delta=1-c^N=1-M^{-2N}.
 \tag{1}
\]
The definition of \(g_n\) applies also to \(n\ge N\).
Every \(g_l\), \(0\le l<N\), is a holomorphic unit near
\(M=1\), for each fixed \(N\).

Use G's actual remaining-head operators \(K,E,F\), with
\(\Omega=FE+qK+q^{-1}K^{-1}\). In particular \(K\) and
\(\Omega\) commute. G proves that the literal finite operator
\(\mathcal A_N=q_FE_\Sigma^d i_d\) is
\[
 \mathcal A_N=H_d(M)K^d\,
 \mathcal F_N(a,b;c;c/(ab)),\quad
 H_d(M)=\prod_{j=1}^d(MQ^{-j}-M^{-1}),
 \tag{2}
\]
where, initially for scalar algebra,
\[
 \Omega=z+z^{-1},\quad a=qKz,\quad b=qK/z,\qquad
 \mathcal F_N(a,b;c;t)=
 \sum_{n=0}^d\frac{(a;Q)_n(b;Q)_n}{f_ng_n(c)}t^n.
 \tag{3}
\]
The scalar notation in (2) is shorthand for its polynomial evaluation
in \(K,\Omega\); it is not a spectral assumption.

The original opposite map is retained in G's exact order
\[
 T=\mathcal B_m(W_\tau^{-1})\,\mathcal A_N\,
                  D_{\rm top}\,\mathscr C_r(M),\qquad
 J=D_N(MK)^{-1}T,
 \tag{4}
\]
where \(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\) has its Laurent-polynomial
continuation, \(r=m-1\), \(\tau=R_1\cdots R_r\), and
\[
 D_{\rm top}=\kappa^r x^{-rd}(x^{-1}Q^{-1})^{\mathsf n},
 \qquad x=-M/q.
\]
Here \(\mathsf n\) is remaining total occupation. The original
\(\kappa\), quotient, turnover, and normalization stay attached to
(4). Every replacement below concerns precisely \(\mathcal A_N\).

## 2. A full-square Fourier interpolation

Set \(u=a^{-1}\), \(v=b^{-1}\), and define the polynomial
\[
 \begin{split}
 \mathcal S_N(u,v;c)
  &:=\mathcal F_N(a,b;c;c/(ab))\\
  &=\sum_{n=0}^d
    \frac{Q^{n(n-1)}c^n(u;Q^{-1})_n(v;Q^{-1})_n}
         {f_ng_n(c)}.
 \end{split}\tag{5}
\]
It has degree at most \(d\) in each variable. The second equality
follows by factoring \((-a)^nQ^{n(n-1)/2}\) from
\((a;Q)_n\), and likewise for \(b\).

Define the finite interpolation polynomials
\[
 L_l(u)=\frac1N\sum_{j=0}^d(uQ^{-l})^j,
 \qquad 0\le l<N.
 \tag{6}
\]
They satisfy \(L_l(Q^k)=\mathbf1_{l=k}\). We claim the exact
whole-meridian identity
\[
 \boxed{\quad
 \mathcal S_N(u,v;c)=
   \sum_{l,k=0}^d C_{lk}(c)L_l(u)L_k(v),\qquad
 C_{lk}(c)=\frac{g_{l+k}(c)}{g_l(c)g_k(c)}.
 \quad}\tag{7}
\]
In particular the square in (7) is not truncated before taking
meridian derivatives.

To prove it, evaluate (5) at \(u=Q^l,v=Q^k\). The finite
Chu identity proved in G gives
\[
 \mathcal S_N(Q^l,Q^k;c)
       =\frac{(cQ^k;Q)_l}{(c;Q)_l}
       =\frac{g_{l+k}(c)}{g_l(c)g_k(c)}.
 \tag{8}
\]
For clarity, its required finite identity is
\[
 \sum_{n=0}^l
 \frac{(Q^{-l};Q)_n(b;Q)_n}{f_n(c;Q)_n}
             (cQ^l/b)^n=\frac{(c/b;Q)_l}{(c;Q)_l}.
\]
After multiplication by \((c;Q)_l\), denote the left side by
\(\mathcal T_l(b,y)\), where \(y=c/b\). Gaussian Pascal gives
\(\mathcal T_{l+1}(b,y)=(1-byQ^l)\mathcal T_l(b,y)
-yQ^l(1-b)\mathcal T_l(bQ,y)\).
Starting with \(\mathcal T_0=1\), induction gives
\(\mathcal T_l=(y;Q)_l\). Thus only products shorter than \(N\)
are divided. Equality on all \(N^2\) grid points proves (7)
by the degree bound, first generically and then holomorphically.

Away from removable denominators, (6) can also be written
\[
 L_l(u)=\frac{1-u^N}{N(1-uQ^{-l})}.
 \tag{9}
\]
Consequently (7) is a double cyclic Cauchy projection. Both Fermat
numerators in (9) remain. Formula (6), not an independently inverted
denominator in (9), defines its matrix values.

More explicitly let \(\mathsf F_{jl}=N^{-1/2}Q^{-jl}\) and
\(\mathbf v(u)=(1,u,\ldots,u^d)\). Then
\[
 \mathcal S_N(u,v;c)=N^{-1}\mathbf v(u)\mathsf F
                      C(c)\mathsf F^{\mathsf t}\mathbf v(v)^{\mathsf t}.
 \tag{10}
\]
This fixes the Fourier normalization and the transpose on the second
leg. Moving these finite transforms in a sewn contraction requires
their corresponding inverse transforms on the exterior.

## 3. Polynomial descent to the actual source

The symmetry \(C_{lk}=C_{kl}\) permits replacement of the summand
in (7) by
\[
 \mathcal D_{lk}(u,v)=
 \tfrac12\{L_l(u)L_k(v)+L_k(u)L_l(v)\}.
 \tag{11}
\]
Every \(\mathcal D_{lk}\) is a symmetric polynomial, hence a
polynomial in \(u+v\) and \(uv\). In the actual variables,
\[
             u+v=\frac{\Omega}{qK},\qquad
             uv=\frac1{QK^2}.
 \tag{12}
\]
Thus (11) defines a literal Laurent polynomial
\(\mathcal D_{lk}(K,\Omega)\), without choosing either root of
\(z+z^{-1}=\Omega\). In particular,
\[
 \boxed{\quad
 \mathcal A_N(M)=H_d(M)K^d
       \sum_{l,k=0}^d C_{lk}(c)\mathcal D_{lk}(K,\Omega).
 \quad}\tag{13}
\]
This is an identity of the original finite matrices. It holds on all
Casimir Jordan blocks and does not require \(u^N=v^N=1\), a
semisimple spectral grid, or an auxiliary scalar geometric substitution.
It can be inserted inside any original marked contraction by linearity,
with all the other factors of (4) and the closing functional retained.
The auxiliary Fourier legs in (10) are not thereby identified with an
orthogonal eigenbasis of the physical heads.

## 4. The cyclic algebra and its original closed contour

The root product identity gives
\[
                    g_{n+N}(c)=\delta g_n(c).
 \tag{14}
\]
Consider the free rank-\(N\) algebra
\[
 \mathcal B_\delta=\mathbb C[y]/(y^N-\delta),\qquad
                 e_l=\frac{y^l}{g_l(c)},\quad 0\le l<N.
 \tag{15}
\]
Coefficients may be holomorphic in the meridian germ. Equation (14)
shows that its multiplication is exactly
\[
          e_l e_k=C_{lk}(c)e_{(l+k)\bmod N}.
 \tag{16}
\]
Let \(\ell_c(e_j)=1\). Define
\[
 U_u(y)=\sum_{l=0}^d L_l(u)\frac{y^l}{g_l(c)},\qquad
 W_c(y)=\sum_{j=0}^d g_j(c)y^{d-j}.
 \tag{17}
\]
Then (7) says \(\mathcal S_N=\ell_c(U_uU_v)\).

This functional has an exact divisor contour. If a positively oriented
circle encloses all zeros of \(y^N-\delta\), then
\[
 \boxed{\quad
 \mathcal S_N(u,v;c)=\frac1{2\pi i}
       \oint\frac{U_u(y)U_v(y)W_c(y)}{y^N-\delta}\,dy.
 \quad}\tag{18}
\]
Indeed on each monomial \(y^j\), \(0\le j<N\), the integral
equals \(g_j(c)\): expand at infinity and select the coefficient
of \(y^{-1}\). The integral annihilates multiples of
\(y^N-\delta\), since the resulting integrand is a polynomial.
It therefore equals \(\ell_c\) on every polynomial modulo that
relation. This proves (18), including products of arbitrary degree.

For \(\delta\ne0\), choose any \(\rho^N=\delta\). The same
cycle is the complete root sum
\[
 \frac1N\sum_{j=0}^d
  \frac{U_u(\rho Q^j)U_v(\rho Q^j)W_c(\rho Q^j)}
       {(\rho Q^j)^d}.
 \tag{19}
\]
Changing the Kummer root \(\rho\) permutes the terms. At
\(\delta=0\), the algebra is nilpotent and (18) is the original
single coefficient residue at zero. No one pole of (19) has been
selected or discarded. A fixed contour may be used on any parameter
set where it encloses the entire divisor and crosses none of it.
For example a radius less than one at \(\delta=0\) does not
automatically work on an \(N\)-uniform scaled meridian collar:
it must still satisfy \(|\delta|<R^N\).

The product law is associative with a useful normal filtration.
For any number of factors, write \(\sum_i l_i=wN+j\),
\(0\le j<N\). Then
\[
 \boxed{\quad
 \prod_i e_{l_i}
       =\delta^w\frac{g_j(c)}{\prod_i g_{l_i}(c)}e_j.
 \quad}\tag{20}
\]
This follows directly from powers of \(y\), so it is independent
of parenthesization. Since \(\delta\) has a simple zero at
\(M=1\), a meridian jet of order \(k\) sees only windings
\(w\le k\). The first normal has the derivative of the zero-winding
coefficient and the one-winding coefficient multiplied by \(2N\);
all higher windings vanish. This statement is for products in this
one coupon algebra with holomorphic coefficients. It does not identify
an arbitrary braid assembly with that algebra, or bound derivatives of
an exterior source.

## 5. The two triangles and the actual first normal

Differentiate in \(\mu=\Log M\), at \(\mu=0\). For \(j<N\), put
\[
 \Sigma_j=\sum_{h=1}^j\frac{Q^h}{1-Q^h},\qquad \Sigma_0=0.
\]
Then \(\partial_\mu g_j/g_j=2\Sigma_j\) at the root, and
\(\delta'=2N\). To distinguish the parameter \(c\) from \(M\), put
\(C^0_{lk}=C_{lk}(Q)\) and
\(\dot C_{lk}=\partial_\mu C_{lk}(Qe^{-2\mu})|_0\).
The exact coupon values and derivatives are
\[
 \begin{array}{ll}
 l+k<N:&
 C^0_{lk}=\dfrac{f_{l+k}}{f_lf_k},\qquad
 \dot C_{lk}=2C^0_{lk}(\Sigma_{l+k}-\Sigma_l-\Sigma_k),\\[2mm]
 l+k=N+j:&
 C^0_{lk}=0,\qquad
 \boxed{\ \dot C_{lk}=2N\dfrac{f_j}{f_lf_k}\ },
 \quad 0\le j\le N-2.
 \end{array}\tag{21}
\]
The second row follows from \(g_{N+j}=\delta g_j\), before
specialization. Thus it is a genuine whole-meridian normal, not the
derivative of a reflected root factorial identity.

The phases can be fixed without choosing an asymptotic branch. Write
\(s_j=\prod_{h=1}^j2\sin(\pi h/N)>0\), with \(s_0=1\).
Since \(f_j=(-i)^jq^{j(j+1)/2}s_j\), (21) becomes
\[
 \begin{split}
 C^0_{lk}&=q^{lk}\frac{s_{l+k}}{s_ls_k},
                  &&l+k<N,\\
 \dot C_{lk}&=2Ni(-1)^{j+1}q^{lk}\frac{s_j}{s_ls_k},
                  &&l+k=N+j.
 \end{split}\tag{22}
\]
In particular the positive sine ratios have an explicit chirp.
One may split \(q^{lk}=q^{(l+k)^2/2}q^{-l^2/2}q^{-k^2/2}\)
by introducing the integer total-output leg. On the upper triangle
that integer is \(N+j\), not silently its residue \(j\).
The phases and the transported exterior remain in the source.

For the actual operator write \(\mathcal D_{lk}(M)\) for (11)--(12)
evaluated on its physical family. The complete product rule is
\[
 \begin{split}
 \mathcal A_N'={}&(H_dK^d)'\sum_{l,k}C_{lk}\mathcal D_{lk}\\
 &+H_dK^d\sum_{l,k}
             (C'_{lk}\mathcal D_{lk}+C_{lk}\mathcal D'_{lk}).
 \end{split}\tag{23}
\]
Each \(\mathcal D'\) is the derivative of its actual ordered matrix
polynomial; no commutation of matrices at different meridians is
assumed. The other factors in (4), including \(D_N(MK)^{-1}\),
the original pivot and any marks, retain their own product-rule terms.

Differentiating the fixed contour (18) retains both numerator
derivatives and
\[
       \frac{\delta' U_uU_vW_c}{(y^N-\delta)^2}.
 \tag{24}
\]
At completeness this is the \(2N/y^{2N}\) denominator contribution.
It is not erased by replacing the entire divisor by its value at zero.
All these derivatives keep \(q=q_N\) fixed; quantum-parameter normals
are outside the statement.

## 6. A uniform bound for the entire upper carry sector

This sector has a quantitative property stronger than a root
first-normal identity. For \(l+k=N+j\), put
\[
 l'=d-l,\qquad k'=d-k,\qquad n'=l'+k'=N-j-2,
 \qquad r_{ab}=\frac{s_{a+b}}{s_as_b}\quad(a+b<N).
 \tag{24a}
\]
The exact reflection \(s_a s_{d-a}=N\) gives
\[
 \frac{s_j}{s_ls_k}
       =\frac1{2N\sin(\pi(j+1)/N)\,r_{l'k'}}.
 \tag{24b}
\]
For fixed \(n<N\), consecutive positive ratios satisfy
\[
 \frac{r_{a+1,n-a-1}}{r_{a,n-a}}
     =\frac{\sin(\pi(n-a)/N)}{\sin(\pi(a+1)/N)}\ge1
                \quad\text{before the midpoint}.
\]
Indeed the difference of these sines is
\(2\cos(\pi(n+1)/(2N))\sin(\pi(n-2a-1)/(2N))\ge0\).
The sequence is symmetric and its two endpoint values are one.
Thus \(r_{ab}\ge1\). Since
\(\sin(\pi(j+1)/N)\ge\sin(\pi/N)\ge2/N\), (21),(24b) imply
\[
           |\dot C_{lk}|\le N/2\qquad(l+k\ge N).
 \tag{24c}
\]

The same sector is polynomially bounded on a whole scaled meridian
collar. F proves, for every fixed \(0<\eta<\pi\), uniform polynomial
bounds on the holomorphic units and their inverses
\[
 h_a(M)=M^{-a}\frac{f_a}{g_a(c)},\qquad
             M=e^{\xi/N},\quad |\xi|\le\eta,\quad 0\le a<N.
\]
The precise identities here are
\[
 \begin{array}{ll}
 l+k<N:&
 C_{lk}(c)=\dfrac{f_{l+k}}{f_lf_k}\dfrac{h_lh_k}{h_{l+k}},\\[2mm]
 l+k=N+j:&
 \boxed{\ C_{lk}(c)=(M^N-M^{-N})
                \dfrac{f_j}{f_lf_k}\dfrac{h_lh_k}{h_j}.\ }
 \end{array}\tag{24d}
\]
They follow directly from (14) and the definition of \(h\).
By (24b), \(|f_j/(f_lf_k)|\le1/4\). Since
\(M^N-M^{-N}=2\sinh\xi\) is bounded on this disk, the entire
upper triangle in (24d) is bounded by \(C_\eta(N+1)^{p_\eta}\).
Cauchy on a slightly larger scaled disk proves polynomial bounds
for every fixed \(\xi\)-derivative. A \(\mu\)-derivative introduces
one further \(N\) per order. No denominator with a zero on the
collar has been divided.

There is also uniform exponential decay in every compact reflected
interior triangle. Suppose \(l',k'\ge\epsilon N\) and
\(l'+k'\le(1-\epsilon)N\), with fixed \(0<\epsilon<1/3\).
Choose \(0<\gamma\le\min(\epsilon/4,\sin(\pi\epsilon)/(4\pi))\).
For sufficiently large \(N\), the first \(\lfloor\gamma N\rfloor\)
ratios in the preceding unimodal sequence are at least two: their
numerator is at least \(\sin(\pi\epsilon)\), and their denominator
is at most \(2\pi\gamma\). All subsequent ratios up to the
smaller of \(l',k'\) are at least one. Hence
\(r_{l'k'}\ge2^{\lfloor\gamma N\rfloor}\). Equations (24b),(24d)
give exponential decay there, up to a polynomial, uniformly on
the collar and for every fixed meridian derivative.

These array bounds also control their scalar Fourier interpolants
on the unit torus. Parseval in (6) gives
\(\sum_l|L_l(u)|^2=1\) when \(|u|=1\). Therefore
\[
 \left|\sum_{l+k\ge N} \dot C_{lk}L_l(u)L_k(v)\right|
 \le\|\dot C_{\rm upper}\|_{\rm F}\le N^2/2,
                       \qquad |u|=|v|=1.
 \tag{24e}
\]
The same argument gives a polynomial bound on the full scaled collar,
and exponential decay for the reflected-interior subarray. More generally,
on \(e^{-R/N}\le |u|,|v|\le e^{R/N}\), Parseval gives
\[
 \|L(u)\|_2^2=N^{-1}\sum_{j<N}|u|^{2j}\le e^{2R},
 \qquad \|\partial_u^pL(u)\|_2\le C_{p,R}N^p.
\]
The derivative estimate follows from the same sum with the falling
factorial \(j(j-1)\cdots(j-p+1)\). Thus every fixed scalar Fourier
jet of the upper interpolant is polynomial on this thin annulus,
jointly with the stated meridian derivatives; the reflected-interior
subarray retains its exponential decay. Fourier variables are held
fixed when differentiating coefficients in \(M\). These are scalar
coefficient-array and scalar-jet estimates. They do not bound arbitrary
evaluated matrix/Jordan norms or conditioned projectors in (13), an
unbounded moving Fourier path, the lower triangle, or the closed source.

On arbitrary scalar arguments the same Parseval sum gives
\(\|L(u)\|_2\le\max(1,|u|)^d\). Thus the entire upper interpolant,
and each fixed meridian derivative, is bounded on the stated collar by
\[
 C(N+1)^p\max(1,|u|)^d\max(1,|v|)^d.
 \tag{24f}
\]
Its possible exponential cost in this scalar bound is entirely in the
two displayed boundary factors; (24f) is not an evaluated operator bound.

## 7. The root arc and affine source rows

At \(c=Q\), define
\[
 \Phi_a(z)=\sum_{n=0}^d\frac{(a;Q)_n}{f_n}z^n.
\]
Coefficient comparison including the last degree proves
\[
 (1-z)\Phi_a(z)-(1-az)\Phi_a(Qz)
                       =-\frac{1-a^N}{N}z^N.
 \tag{25}
\]
Iterate this row around the finite clock. The transport product is
\((1-a^Nz^N)/(1-z^N)\). Dividing on a generic set and cancelling
the full orbit factors gives the all-polynomial formula
\[
 \Phi_a(z)=\frac1N\sum_{k=0}^d
       \prod_{j=0}^{k-1}(1-aQ^jz)\prod_{j=k+1}^{d}(1-Q^jz).
 \tag{26}
\]
Polynomial continuation proves it at every omitted divisor. In (3)
with \(c=Q\), the exact original Hadamard contour is
\[
 \mathcal F_N(a,b;Q;t)
       =\operatorname{CT}_z\Phi_a(z)\Phi_b(t/z),
                   \qquad abt=Q.
 \tag{27}
\]
The two numerator activities satisfy \((az)(bt/z)=Q\) exactly.
They cannot both belong to disks of radius less than one. Changing
the coefficient-circle radius does not delete this reciprocal interface.

Equivalently, the root coefficient array in (7) has generating
polynomial
\[
 P_N(X,Y)=\sum_{l+k<N}\frac{f_{l+k}}{f_lf_k}X^lY^k.
\]
Gaussian Pascal, including the total-degree-\(N\) boundary, gives
\[
 \boxed{\ (1-X)P_N(X,Y)-YP_N(QX,Y)=1-X^N-Y^N.\ }
 \tag{28}
\]
The internal degree-\(N\) coefficients vanish because
\({N\brack l}_Q=0\) for \(0<l<N\); the two corner terms remain.
With \(T_Qf(X)=f(QX)\), this also follows from
\(P_N=\sum_{n<N}(X+YT_Q)^n1\) and
\((X+YT_Q)^N=X^N+Y^N\). This affine Fermat row describes the
root coupon value. Its whole-meridian normal is (21), not a
homogeneous continuation of (28).

## 8. A literal one-head calibration and the remaining scope

The moving coupons in (23) matter even on one actual tail head.
On its occupation \(j\), the displayed balanced arrows give
\(\Omega(M)=-M-M^{-1}\) and \(K_j(M)=-Mq^{-1}Q^{-j}\).
Choosing \(z=-M\) in the scalar calculation gives
\(u=M^{-2}Q^j,v=Q^j\). The terminating Chu identity therefore gives
the exact value of the normalized factor
\[
 \mathcal S_N(M^{-2}Q^j,Q^j;M^{-2}Q)
       =\frac{(M^{-4}Q^{j+1};Q)_j}{(M^{-2}Q;Q)_j}.
 \tag{29}
\]
If \(2j\ge N\), its root value is zero. The numerator contains
exactly one factor \(1-M^{-4}\); all other factors and the
denominator are units at the root. Its true \(\mu\)-derivative is
\[
                 4N\frac{f_{2j-N}}{f_j^2}.
 \tag{30}
\]
This is twice the fixed-grid coefficient normal in (21); the moving
polynomial coupon supplies the rest. At \(j=d\), the complete
root sum is zero although its \(n=d\) summand in (3) is exactly
\(Q\), and (30) equals \(4/(1-Q^{-1})\). These follow by
\(f_d=N\) and \(f_{d-1}=N/(1-Q^{-1})\). This is an all-level
actual-head calibration, not a claim about a knot contribution.

Equations (7),(13),(18),(20) give an associative, finite Fourier and
closed-divisor presentation of the same actual Gauss factor, with
its source normalization and all first-normal carries. Section 6 also
bounds the entire upper coefficient sector on a scaled meridian collar.
These conclusions do not supply a relative estimate after contraction with
\(\mathcal D_{lk}(K,\Omega)\), the factors of (4), or an exterior.
The known concavity of the positive triangle weight is not a new
conclusion here and does not remove its chirp. Nor does (19) choose
one Kummer root as a contributing geometric period. The actual
reconstructed kernel asymptotic and its source pairing remain open.

## Complete proof directs

* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* F: notes/research_actual_meridian_source_frames.md,
  SHA256 6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.

Both complete directs and the entire final were read nontruncated in this
author sequence; used implications and pins were checked. Only written
mathematics and text/hash operations were used. Frozen and public files
were not edited.
