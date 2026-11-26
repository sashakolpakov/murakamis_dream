# An exact outgoing equation for the first cardinal correction

Research deduction, 7 November 2026. The complete first-node selected
correction satisfies a finite polynomial difference equation driven
by an original two-vertex conditional source. The driving source is
at the opposite physical ordinary color, with its original endpoint
normalization. This identifies the complete outgoing observation,
including its top-row forcing and its one-dimensional homogeneous
part, before estimating any of its rows.

No numerical evaluation is used. This note proves an exact source
identity, not suppression of either complete Fourier sector.

## 1. The driving polynomial is an original source

Keep
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\qquad N\ge2 .
 \tag{1}
\]
Let \(d_N\) be the original degree-\(D\) polynomial with
\(d_N(r^b)=P_b^{-1}\). The conditional kernels are
\[
 C_{\beta,N}(Y,Z)
   =\sum_{j=0}^{D}
      \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
                   \qquad \beta=0,1.
 \tag{2}
\]
Write \(\gamma=MJM^3e_0\), \(v_j=(-q)^{-j}\gamma_j\), with
the original matrices and endpoint values
\(\gamma_D=N\) and \(\gamma_0=\kappa(M^3e_0)_D\).
Define the complete outgoing polynomial
\[
 V_{\beta,N}(Z)=\sum_{j=0}^{D}v_j\psi_{\beta,j}(Z),
 \qquad
 \psi_{\beta,j}(Z)=\frac{p_j(Z)}{P_j^{1+\beta}} .
 \tag{3}
\]

Put \(c_0=2\cos(\pi/N)\), the first physical ordinary node.
The original Newton evaluation vector at \(c_0\) is exactly \(e_0\).
Consequently the whole cap polynomial from
[conditional torus composition, equation (21)](research_mixed_conditional_torus_composition.md)
satisfies
\[
 H_N(c_0,r^{-j})=1,\qquad
 U_{0,N}(c_0,Y)=\sum_{j=0}^{D}\frac{p_j(Y)}{P_j}
                           =N d_N(Y).
 \tag{4}
\]
Here the first equality follows from the complete Newton definition
of \(H_N\), not from an asymptotic at the limiting color \(+2\).
For a direct check of the second equality at \(Y=r^b\), use
\[
 \sum_{j=0}^{D}\frac{p_j(r^b)}{P_j}
 =\frac1{P_b}\sum_{j=0}^{D-b}(r^{j+1};r)_b
 =\frac N{P_b}.
 \tag{5}
\]
The polynomial \((rZ;r)_b\) has degree \(b<N\) and constant
coefficient one. Its sum over all \(N\) roots is \(N\);
the terms removed from the last sum vanish exactly. Both sides
of (4) have degree at most \(D\), so their physical values
determine the same polynomial.

Let
\[
 \mathcal F_{\beta,N}^{\,\mathrm{opp}}(Z)
   =N\operatorname{CT}_Y
          [U_{0,N}(c_0,Y)C_{\beta,N}(Y,Z)] .
 \tag{6}
\]
This is the full original conditional message for the word
\(3(3+\beta)\) at ordinary color \(c_0\); in particular it is
not the ordinary-color evaluation of its second boundary.
The exact moment identification in
[the coherent-response theorem, Proposition 1](research_mixed_next_low_cardinal_coherent_response.md)
is
\[
 \operatorname{CT}_Y[d_N(Y)Y^{-j}p_j(Y)]
       =\frac{P_jv_j}{\kappa^2N^2}.
 \tag{7}
\]
Equations (4), (6), and (7) prove the full identity
\[
       \boxed{\quad
       V_{\beta,N}=\kappa^2\mathcal F_{\beta,N}^{\,\mathrm{opp}}.
       \quad}
 \tag{8}
\]
Every finite row, support zero, and original normal coordinate is
retained in (6)--(8).

## 2. Finite outgoing difference operators

For a polynomial \(f(Z)\), set
\[
 T_+f(Z)=f(rZ),\qquad T_-f(Z)=f(r^{-1}Z),\qquad
 \mathcal Lf(Z)=\frac{f(Z)-f(r^{-1}Z)}Z,
 \qquad
 \mathcal D=T_+(I-\mathcal L).
 \tag{9}
\]
The apparent quotient at \(Z=0\) is removable. These operators
preserve the polynomial source, and \(\mathcal L\) lowers its
degree. Define
\[
                   \mathcal L_\beta=(I-r\mathcal D)^\beta
                                                 \mathcal L .
 \tag{10}
\]
Their exact actions on the original outgoing basis are
\[
 \begin{split}
 \mathcal D\psi_{\beta,j}&=r^j\psi_{\beta,j},\\
 \mathcal L_\beta\psi_{\beta,j}&=\psi_{\beta,j-1}
                      &&(j\ge1),\\
 \mathcal L_\beta\psi_{\beta,0}&=0 .
 \end{split}
 \tag{11}
\]
To verify this, the finite products give
\[
 p_j(Z)-p_j(r^{-1}Z)
      =(1-r^j)Zp_{j-1}(Z),\qquad
 (I-\mathcal L)p_j=r^jp_j(r^{-1}Z).
 \tag{12}
\]
The first identity yields
\(\mathcal L\psi_{\beta,j}
=(1-r^j)^{-\beta}\psi_{\beta,j-1}\).
On that latter basis element the factor in (10) is
\((1-r^j)^\beta\). The second identity in (12) proves
the diagonal statement in (11), independently of the normalization
of \(p_j\).

## 3. The complete selected and unselected corrections

Let \(a_j\) be the exact first-node cumulative coefficients:
\[
 a_0=1-\frac{\gamma_0}{\kappa^2N^2},\qquad
 a_j-a_{j-1}
  =-\frac{1}{\kappa^2N^2}
       \left(v_j+\frac{r^j}{1-r^j}v_{j-1}\right).
 \tag{13}
\]
By the exact cardinal-sector theorem,
\[
 S_{\beta,N}(Z):=\mathcal S_{1,\beta}[\mathfrak l_0](Z)
        =\sum_{j=0}^{D}a_j\psi_{\beta,j}(Z),
 \qquad
 \mathcal S_{0,\beta}[\mathfrak l_0]
        =C_{\beta,N}(1,Z)-S_{\beta,N}(Z).
 \tag{14}
\]
These are the complete Fourier coefficients, with the factor \(N\)
already included in their definition. The moment proof of (13)--(14)
is in
[the coherent-response theorem, equations (14)--(15)](research_mixed_next_low_cardinal_coherent_response.md);
it retains the forced initialization.

**Theorem 1.** At every level of either parity, \(S_{\beta,N}\)
is the unique polynomial of degree at most \(D\) satisfying
\[
 \boxed{\begin{split}
 &(I-r\mathcal D)(I-\mathcal L_\beta)S_{\beta,N}\\
 &\quad=\frac1{\kappa^2N^2}
     \left\{(I-r\mathcal D)\mathcal L_\beta V_{\beta,N}
              +r\mathcal D V_{\beta,N}
              -v_D\psi_{\beta,D}\right\},\\
 &S_{\beta,N}(r^{-1})
              =1-\frac{\gamma_0}{\kappa^2N^2},
 \qquad v_D=N(-q)^{-D}.
 \end{split}}
 \tag{15}
\]
Equivalently the driving terms are
\[
 \frac1{N^2}
    \{(I-r\mathcal D)\mathcal L_\beta
                      +r\mathcal D\}
                \mathcal F_{\beta,N}^{\,\mathrm{opp}}
       -\frac{(-q)^{-D}}{\kappa^2N}\psi_{\beta,D}.
 \tag{16}
\]
The second, unselected sector satisfies the same equation with
the right side negated and boundary value
\(\gamma_0/(\kappa^2N^2)\).

*Proof.* For \(0\le j<D\), the coefficient of
\(\psi_{\beta,j}\) in the left side of (15) is
\[
               (1-r^{j+1})(a_j-a_{j+1}).
 \tag{17}
\]
Its coefficient in the right side is
\[
 \frac1{\kappa^2N^2}
       \{(1-r^{j+1})v_{j+1}+r^{j+1}v_j\},
 \tag{18}
\]
which agrees by (13). The top coefficient on the left vanishes
because \(r^{D+1}=1\). On the right,
\(r\mathcal D(v_D\psi_{\beta,D})=v_D\psi_{\beta,D}\);
the last forcing term cancels it exactly. Thus it cannot be
dropped even though it has polynomial size.

Since \(p_j(r^{-1})=0\) for \(j\ge1\), evaluation at \(r^{-1}\)
recovers \(a_0\), proving the boundary condition.
The factors \(1-r^{j+1}\) in (17) are all nonzero for \(j<D\).
Thus the equation fixes every difference \(a_j-a_{j+1}\),
and its homogeneous polynomial solutions have constant basis
coefficients. Their span is precisely
\[
       \sum_{j=0}^{D}\psi_{\beta,j}(Z)=C_{\beta,N}(1,Z),
 \tag{19}
\]
whose value at \(r^{-1}\) is one. The boundary value therefore
fixes the unique polynomial solution. Equation (8) gives (16).
Finally (19) is annihilated by the left operator, and subtracting
(15) from it proves the unselected assertion. \(\square\)

The displayed operators may be written as finite combinations of
the shifts \(Z\mapsto r^kZ\) with rational coefficients whose apparent
singularities at zero cancel on polynomials. No outgoing interpolation
of the discrete asymptotic was used. In particular (15) retains all
indices beyond the real interval in the
[endpoint packet](research_mixed_next_low_cardinal_endpoint_packet.md).

## 4. Scope of the reduction

Equation (15) replaces the cumulative observation by a complete
forced outgoing difference problem, with an original driving word
and one fixed boundary value. The opposite ordinary color is the
actual \(N\)-dependent node \(c_0\), not the complete color \(-2\).
The right side is a conditional message, not an ordinary boundary
evaluation of a two-boundary kernel. An ordinary packet near the
complete colors does not by itself estimate (16) on the next
Fourier-reference domains.

The coefficient equation (17) has only polynomial small-denominator
cost, but a bound on its Newton coefficients is not a bound of the
same rate on their signed outgoing sum. Neither a polynomial
inverse estimate in an outgoing function norm nor a separate
sector-suppression estimate is asserted here.
The top-row forcing and the homogeneous component in (15) remain
part of that analytic problem.

All identities are finite polynomial identities at both parities.
They preserve the original matrices and Frobenius normal data.
Fixed outgoing derivatives can be taken in these identities;
they do not imply a bound for the complete outgoing derivatives
without a complete source estimate.
