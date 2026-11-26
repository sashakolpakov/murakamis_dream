# The coherent response inside a low cardinal sector

Research deduction, 7 November 2026. The divided-difference correction
for a low physical incoming index has exact moments in the original
three-crossing Fourier column. At the first node its two complete
sectors are complementary cumulative observations of that column.
The known nonzero column asymptotic proves that their normalized
individual rows are not polynomially bounded.

This rules out a coefficientwise shortcut to the low-sector estimate.
It does not give a lower bound for either complete outgoing polynomial:
the remaining outgoing sum is coherent, and its cancellation is not
estimated here. No numerical evaluation is used.

## 1. The exact moments and the original column

Put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,\quad S_j=|P_j|,
 \quad p_j(Y)=(rY;r)_j,\quad \rho_j(Y)=Y^{-j}p_j(Y).
 \tag{1}
\]
The polynomial \(d=d_N\) has degree at most \(D\) and satisfies
\(d(r^b)=P_b^{-1}\). Use precisely the sector functionals and
cardinal polynomials of
[exact sector separation](research_mixed_next_cardinal_sector_separation.md):
\[
 \begin{split}
 C_\beta(Y,Z)&=\sum_{j=0}^{D}
                 \rho_j(Y)p_j(Z)/P_j^{2+\beta},\\
 \mathcal S_{\sigma,\beta}[E]
     &=N[Y^{\sigma N}]\{E(Y)d(Y)C_\beta(Y,Z)\},
                        \quad\sigma=0,1,\\
 \mathfrak l_b(Y)&=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu .
 \end{split}
 \tag{2}
\]
For \(B=r^b\), define the polynomial and its complete moments
\[
 K_B(Y)=B\,\frac{d(Y)-d(B)}{Y-B}=NQ_b(Y),\qquad
 A_j(B)=\operatorname{CT}_Y[K_B(Y)\rho_j(Y)],
 \qquad
 M_j=\operatorname{CT}_Y[d(Y)\rho_j(Y)] .
 \tag{3}
\]
The apparent pole of \(K_B\) is removable, and its degree is at
most \(N-2\). The original exact two-sector identities are
\[
 \begin{split}
 \mathcal S_{1,\beta}[\mathfrak l_b]
       &=\sum_{j=0}^{D}A_j(B)\frac{p_j(Z)}{P_j^{2+\beta}},\\
 \mathcal S_{0,\beta}[\mathfrak l_b]
       &=P_b^{-1}C_\beta(B,Z)
                    -\mathcal S_{1,\beta}[\mathfrak l_b].
 \end{split}
 \tag{4}
\]
In particular no additional scalar \(N\) belongs in the first line
after \(K_B=NQ_b\) is used.

Let \(M\) and \(J\) be the original crossing and reversal matrices,
and let \(e_0\) be the first coordinate vector. Define
\[
                       \gamma=MJM^3e_0.
 \tag{5}
\]
This is the complete coherent column studied in
[the next-crossing Fourier theorem](research_three_crossing_next_crossing_fourier.md),
not a replacement boundary evaluation.

**Proposition 1.** At every \(N\ge2\), both parities, and every
\(0\le j<N\),
\[
             \boxed{\quad
             M_j=\frac{(-q)^{-j}P_j}{\kappa^2N^2}\gamma_j .
             \quad}
 \tag{6}
\]

*Proof.* The Laurent band of \(d\rho_j\) is \([-j,D]\).
Its only frequency divisible by \(N\) is zero, so
\[
 N M_j=\sum_{i=0}^{D}
                  \frac{r^{-ij}p_j(r^i)}{P_i}=L_1(j,0).
 \tag{7}
\]
The last equality is the literal weighted conditional sum in
[conditional leg summation](research_mixed_conditional_leg_sum.md),
equations (1) and (5), including its exact zeros for \(i+j\ge N\).
The original matrix identities are
\[
 \Gamma B_4=\kappa^2N T_1,\qquad
 (T_1)_{j0}=L_1(j,0)/P_j^2,\qquad
 \Gamma B_4=S A_4S^{-1},
 \tag{8}
\]
where \(A_n=JM^n\). The full basis change in
[the lowered-word observation](research_mixed_next_lowered_word_dual_observation.md),
equations (1)--(3), is
\[
 S=L M,\qquad L_{jj}=\kappa^{-1}(-q)^{-j}/P_j.
 \tag{9}
\]
Since \(L^{-1}e_0=\kappa e_0\) and \(A_4M^{-1}=A_3\),
\[
 (\Gamma B_4)e_0
       =\kappa S A_3e_0=\kappa L\gamma.
 \tag{10}
\]
Combine (7)--(10). The \(j\)-th entry is
\(\kappa^2N^2M_j/P_j^2=(-q)^{-j}\gamma_j/P_j\),
which is (6). All products and transposes are the original
bilinear ones. \(\square\)

The finite moment recurrence also retains this column:
\[
 \begin{split}
 A_0(B)&=d(B)-\widehat d_0,\qquad
                  \widehat d_0=[Y^0]d=M_0,\\
 A_j(B)&=(B^{-1}-r^j)A_{j-1}(B)
                           -M_j-r^jM_{j-1},\qquad 1\le j<N.
 \end{split}
 \tag{11}
\]
Indeed \(\rho_j=(Y^{-1}-r^j)\rho_{j-1}\), and
\[
 \frac{B}{Y(Y-B)}=\frac1{Y-B}-Y^{-1}.
 \tag{12}
\]
The term \(d(B)Y^{-1}\rho_{j-1}\) has zero constant
coefficient. The remaining additional moment is
\(\operatorname{CT}(dY^{-1}\rho_{j-1})=M_j+r^jM_{j-1}\).
This proves (11), including the constant row.

## 2. The first node and the forced shift between subsequent nodes

For \(b=0\), one has \(B=P_b=1\) and \(\rho_j(1)=P_j\).
Put
\[
        a_j=\frac{A_j(1)}{P_j},\qquad
        v_j=(-q)^{-j}\gamma_j .
 \tag{13}
\]
Equations (6) and (11) give the exact cumulative response
\[
 \boxed{\begin{split}
 a_0&=1-\frac{\gamma_0}{\kappa^2N^2},\\
 a_j-a_{j-1}
   &=-\frac1{\kappa^2N^2}
          \left\{v_j+\frac{r^j}{1-r^j}v_{j-1}\right\},
                      \qquad1\le j<N.
 \end{split}}
 \tag{14}
\]
Consequently the complete first-node sectors are
\[
 \boxed{\begin{split}
 \mathcal S_{1,\beta}[\mathfrak l_0](Z)
       &=\sum_{j=0}^{D}a_j\frac{p_j(Z)}{P_j^{1+\beta}},\\
 \mathcal S_{0,\beta}[\mathfrak l_0](Z)
       &=\sum_{j=0}^{D}(1-a_j)\frac{p_j(Z)}{P_j^{1+\beta}} .
 \end{split}}
 \tag{15}
\]
Their sum is exactly \(C_\beta(1,Z)\), coefficient by coefficient
in the original outgoing Newton basis. The two coherent response
terms in (15) have not been estimated separately.

There is a complementary forced identity in the incoming index.
Let
\[
 f(Y)=\frac{Y(1-Y^N)}{N^2(1-Y)},\qquad
 g_b(Y)=P_bK_{r^b}(Y)=NP_bQ_b(Y).
 \tag{16}
\]
For \(1\le b<N\), the original forced equation for \(d_N\)
implies
\[
 \boxed{\quad
 g_b(Y)=g_{b-1}(r^{-1}Y)
       +P_{b-1}r^b
                 \left\{d(Y)-\frac{f(Y)}{Y-r^b}\right\}.
 \quad}
 \tag{17}
\]
To check it, use
\[
 d(r^{-1}Y)=(1-Y)d(Y)+f(Y),\quad
 d(r^{b-1})=(1-r^b)d(r^b),\quad
 P_b=(1-r^b)P_{b-1}
 \tag{18}
\]
inside \(g_{b-1}(r^{-1}Y)\). Since \(f(r^b)=0\) for
\(b\ge1\), the displayed quotient is a polynomial. Its
degree-\(D\) coefficient equals \(1/N^2=[Y^D]d\), so the
difference in braces has degree at most \(N-2\), as required.
At \(b=0\), the forcing has \(f(1)=1/N\); thus (17) is not
an unforced initialization rule for \(g_0\).

These identities isolate the actual complete column and endpoint
forcing inside every low-index defect. They do not replace the
coherent observations of the shifted functions in (17) by their
physical values.

## 3. A proved obstruction to a uniform polynomial row bound

The original theorem for \(\gamma\) gives a nonzero asymptotic
with its fixed endpoint normalization. For \(0<t<1/2\), use its
notation
\[
 \begin{split}
 X(t)&=e^{-2\pi it},\qquad
 d_*(t)=4\sin^2\pi t=2-X-X^{-1},\\
 \lambda(t)&=\frac{3-2X+\sqrt{4/X-3}}2,\\
 I(t)&=\int_0^t\log\lambda(u)\,du,\qquad
 A(t)=\Re I(t)-2J(t).
 \end{split}
 \tag{19}
\]
The branches are exactly those of that theorem. Its equations
(4)--(10) state
\[
 \begin{split}
 y_j&=\frac{S_j^2v_j}{\gamma_0}
        =G(j/N)e^{NI(j/N)}(1+O(N^{-1})),\\
 |\gamma_0|&=N^{3/2}(1+O(N^{-1})),
 \end{split}
 \tag{20}
\]
uniformly on each compact real subinterval of \((0,1/2)\),
with \(G\) nonzero. The uniform factorial asymptotic gives,
on the same compact intervals,
\[
 |v_j|\asymp N^{1/2}e^{NA(j/N)},\qquad
 \frac{v_{j-1}}{v_j}
       =\frac{d_*(j/N)}{\lambda(j/N)}+O(N^{-1}).
 \tag{21}
\]
The ratio assertion follows directly by dividing the two
consecutive nonzero formulas in (20), and using
\(S_j^2/S_{j-1}^2=d_*(j/N)\).

Substitution in the exact increment (14) yields
\[
 a_j-a_{j-1}
   =-\frac{v_j}{\kappa^2N^2}
       \left\{1-\frac{1-X(j/N)}{\lambda(j/N)}
                                      +O(N^{-1})\right\}.
 \tag{22}
\]
Its leading bracket is nonzero throughout \(0<t<1/2\).
Indeed \(\lambda\) solves the original characteristic equation
\[
 \lambda^2-(3-2X)\lambda+d_*(t)(1-X)=0.
 \tag{23}
\]
At \(\lambda=1-X\), the left side is
\[
                        -\frac{1-X}{X}\ne0.
 \tag{24}
\]
On every fixed compact subinterval the bracket is consequently
bounded away from zero.

**Proposition 2.** There is a constant \(c>0\) such that, with
\(j_N=\lfloor N/4\rfloor\) and all sufficiently large \(N\)
of either parity,
\[
 \max\{|a_{j_N}|,\ |a_{j_N-1}|\}
       \ge cN^{-3/2}e^{NA(1/4)},\qquad A(1/4)>0.
 \tag{25}
\]
Thus no constants \(C,K\) can give
\[
              |A_j(1)|\le C N^K S_j
                         \quad\hbox{for all }0\le j<N
 \tag{26}
\]
at all sufficiently large levels.

*Proof.* The original dominant-profile theorem proves that \(A\)
increases from \(A(0)=0\) to its unique maximum \(x_*\).
Its exact cubic characterization has
\(2\cos(2\pi x_*)\in(-2,-1)\), so \(x_*>1/3\).
It follows without evaluating the action that \(A(1/4)>0\).
Equations (21)--(24), in a fixed neighborhood of \(1/4\),
give
\[
 |a_{j_N}-a_{j_N-1}|
       \ge c_1N^{-3/2}e^{NA(j_N/N)}
       \ge c_2N^{-3/2}e^{NA(1/4)}.
 \tag{27}
\]
The last step uses the bounded derivative of \(A\) and
\(|j_N/N-1/4|\le1/N\). At least one of the two terms has
modulus at least half that difference. Since
\(|A_j(1)|/S_j=|a_j|\), this proves (25)--(26).
\(\square\)

For the index realizing (25), the other sector coefficient
\(1-a_j\) has the same positive exponential lower rate, by
\(|1-a_j|\ge|a_j|-1\). Both normalized row families in (15)
therefore exhibit exponential growth, even though their sum
has coefficient exactly one at every row.

This is a statement about actual coefficients in the specified
finite Newton source. It supplies no lower bound for
\(\mathcal S_{\sigma,\beta}[\mathfrak l_0](Z)\) on an output
domain: different \(j\)-terms in either line of (15) can still
cancel. In particular it is not a counterexample to a possible
whole-sector bound on the actual matched next-reference families.

## 4. Placement in the low physical interval

The original lowered-word formula for the complete prefix is
\[
 F_{34,N}(w,r^b)
       =\frac{(-q)^bP_b}{\kappa^2N}\ell_{b,N}(w),
 \qquad \ell_{b,N}(w)=(v(w)^TA_3^2)_b.
 \tag{28}
\]
For the exact low cardinal correction
\(E_{\rm low}=\sum_{b\le\lfloor\delta N\rfloor}
 F_{34,N}(w,r^b)\mathfrak l_b\), equations (4) and (28) give
\[
 \mathcal S_{1,\beta}[E_{\rm low}]
   =\frac1{\kappa^2N}
      \sum_{b=0}^{\lfloor\delta N\rfloor}(-q)^b\ell_{b,N}(w)
       \sum_{j=0}^{D}
            P_bA_j(r^b)\frac{p_j(Z)}{P_j^{2+\beta}}.
 \tag{29}
\]
The other sector is its negative plus the already bounded
combined physical sum
\[
 \frac1{\kappa^2N}
     \sum_{b=0}^{\lfloor\delta N\rfloor}
             (-q)^b\ell_{b,N}(w)C_\beta(r^b,Z).
 \tag{30}
\]
The [low physical interval theorem](research_mixed_next_low_physical_interval.md)
controls (30), with all ordinary derivatives and both parities.
It does not estimate (29).

Every identity above is finite and retains all rows, phases,
factorials, endpoint forcing and original first-normal data.
It may be differentiated in the ordinary color and outgoing
variable before or after the displayed finite operations.
The obstruction (25) concerns an internal coefficient at \(b=0\);
it does not alter those derivative conventions.

The useful exact reduction is (6), (14), and (29): a separate
low-sector estimate must control a cumulative observation of the
known coherent column \(\gamma\), or reorganize its full outgoing
sum. A polynomial bound on each normalized defect row is already
excluded by the original source asymptotic. No uniform lower or
upper bound for that remaining complete observation is claimed.
