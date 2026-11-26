# A closed difference equation for the twice-crossed conditional sum

Research deduction, 7 November 2026. The complete conditional polynomial
obtained after two negative crossings satisfies a second-order difference
equation in its incoming parameter. Its forcing is an explicit product
of two cyclotomic factors. These factors are retained before every
specialization. The equation also recovers the quadratic critical-point
equation, with the incoming exponential derivative specified explicitly.

This is an equation for the original finite boundary function. It is
not an identification with a knot's peripheral A-polynomial, and it
does not establish dominance of the conditional critical point.

## 1. The finite sum and its ordered operator

Let \(N\ge2\), \(r=e^{-2\pi i/N}\), \(D=N-1\), and
\[
 P_j=(r;r)_j,\qquad
 p_j(W)=(rW;r)_j,\qquad
 \rho_j(X)=X^{-j}(rX;r)_j
            =\prod_{k=1}^j(X^{-1}-r^k).
 \tag{1}
\]
Thus \(P_0=1\), \(P_D=N\), and \(\rho_N=X^{-N}-1\).
The complete polynomial is
\[
 F_N(X,W)=C_{0,N}(X,W)
       =\sum_{j=0}^{D}\frac{p_j(W)}{P_j^2}\rho_j(X).
 \tag{2}
\]
It is the exact source appearing in equation (14) of
[the negative-crossing reduction](research_mixed_fourier_negative_crossing_full_sources.md).
In that application \(X=e^{-2\pi ia}\) and \(W=e^{-2\pi iy}\).

Write \((T_X f)(X)=f(rX)\), and define
\[
 \mathsf D=(1-rX)T_X+rX,\qquad Zf=X^{-1}f.
 \tag{3}
\]
Multiplications and shifts act from right to left. In particular,
coefficients to the left of \(\mathsf D\) in the following formula
are not shifted by it. The elementary product identities give
\[
 \mathsf D\rho_j=r^{-j}\rho_j,\qquad
 (Z-r\mathsf D^{-1})\rho_j=\rho_{j+1},\qquad
 \mathsf DZ=r^{-1}Z\mathsf D+(r-1).
 \tag{4}
\]
The raising identity is used for \(0\le j<N\). Its inverse is defined on
\(\operatorname{span}(\rho_0,\ldots,\rho_N)\), where all its
eigenvalues are nonzero. The final equation below has no inverse
operator. This is the same Newton-basis raising identity used in
[the Gram transport formula](research_mixed_terminal_gram_shift.md).

**Theorem 1.** Define the ordered second-order operator
\[
 \boxed{\quad
 \mathcal L_{N,W}
   =(1-r^{-2}X^{-1})\mathsf D^2
       +(r^{-1}-2+Wr^{-1}X^{-1})\mathsf D+1-W.
 \quad}
 \tag{5}
\]
At every level, the complete finite sum satisfies
\[
 \boxed{\quad
 \mathcal L_{N,W}F_N(X,W)
      =-\frac{(1-W^N)(X^{-N}-1)}{N^2}.
 \quad}
 \tag{6}
\]
The identity holds for every complex \(W\) and every nonzero \(X\),
including all physical incoming nodes and all physical values of \(W\).

*Proof.* Put \(a_j=p_j(W)/P_j^2\) and
\(E=\mathsf D^{-1}\). The coefficients obey
\[
        (1-r^j)^2a_j=(1-r^jW)a_{j-1},\qquad 1\le j<N.
 \tag{7}
\]
Apply the raising identity in (4) to the entire finite sum. Equations
(7), including the actual last raised term, give
\[
 \bigl\{(1-E)^2-(1-WE)(Z-rE)\bigr\}F_N
                    =-(1-W)a_D\rho_N.
 \tag{8}
\]
The coefficient with index zero is zero on both sides before the
last term is added. There is no term with a denominator \(P_N\).
Instead,
\[
       (1-W)a_D=\frac{1-W^N}{N^2}
 \tag{9}
\]
is the finite product identity, valid also at \(W=1\).

For clarity one can clear the inverse using the equivalent ordering
\((1-WE)(Z-rE)=(Z-rE)(1-rWE)\) on these basis vectors.
From (4),
\[
 \mathsf D^2 Z=r^{-2}Z\mathsf D^2+(r-r^{-1})\mathsf D.
 \tag{10}
\]
Multiplication of (8) on the left by \(\mathsf D^2\), followed by
(10), gives precisely (5). On the right,
\(\mathsf D^2\rho_N=\rho_N\), because \(r^N=1\).
Equation (9) now proves (6). \(\square\)

The same operator has an exact telescoping identity before the
physical sum is taken. Use the original factorial and reciprocal
continuations \(\Pi_N,E_N\) from
[the complete endpoint-current construction](research_mixed_three_fourier_conditional_endpoint_current.md),
and put
\[
 \begin{split}
 T_N(s;a,y)
   &=e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+y)
                        E_N(a)E_N(y)E_N(s)^2,\\
 B_N(s;a,y)&=(e^{2\pi is}-1)^2T_N(s;a,y).
 \end{split}
 \tag{10a}
\]
Where these functions are regular, the undivided factorial recurrences
give
\[
 \mathsf D_XT_N(s)=e^{2\pi is}T_N(s),\qquad
 (1-rU)^2T_N(s+1/N)
       =X^{-1}(1-rXU)(1-rWU)T_N(s),
 \quad U=e^{-2\pi is}.
 \tag{10b}
\]
Substituting these two identities into (5) proves
\[
 \boxed{\quad
 \mathcal L_{N,W}T_N(s;a,y)
                    =B_N(s;a,y)-B_N(s+1/N;a,y).
 \quad}
 \tag{10c}
\]
Both sides extend across removable singularities by the same original
factorial identities. In particular,
\[
 B_N(0)=0,\qquad
 B_N(1)=\frac{(1-W^N)(X^{-N}-1)}{N^2}.
 \tag{10d}
\]
For the second value, the identity
\[
 B_N(s)=e^{2\pi iNas}e^{4\pi is}
      \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s-1/N)^2
\]
removes the double reciprocal pole at \(s=1\). Now use
\(\Pi_N(1+a)E_N(a)=1-X^N\), the analogous identity at \(y\),
and \(E_N(1-1/N)=1/N\). Thus summing (10c) at all physical
indices telescopes to precisely the forcing in (6). For a contour
integral the shifted boundary pieces must likewise be retained;
the telescoping identity does not make them zero.

## 2. What the equation determines at roots of unity

Consider the Laurent-polynomial space
\[
        \mathscr B_N=\operatorname{span}\{\rho_0,\ldots,\rho_D\}
                    =\operatorname{span}\{1,X^{-1},\ldots,X^{-D}\}.
 \tag{11}
\]
The coefficient of \(\rho_0\), denoted \(a_0\), specifies the
normalization used here; it is not the coefficient of \(X^0\).

**Corollary 2.** If \(W^N\ne1\), equation (6) has exactly one
solution in \(\mathscr B_N\), namely (2). If \(W^N=1\), its
right-hand side vanishes and its solution space in \(\mathscr B_N\)
is one-dimensional. The extra condition \(a_0=1\) again selects (2).

*Proof.* Clear \(\mathsf D^2\) in (8); it is invertible on the
space with the one added vector \(\rho_N\). Comparing the
coefficients \(\rho_1,\ldots,\rho_D\) forces (7), so every
candidate is \(a_0F_N\). Its last coefficient in (8) is
\(-a_0(1-W^N)/N^2\). When \(W^N\ne1\), equation (6)
therefore forces \(a_0=1\). When \(W^N=1\), this final equation
is identically zero. No other freedom remains, because
\(1-r^j\ne0\) for \(1\le j<N\). \(\square\)

Thus specialization can remove the forcing without removing the
finite source. Keeping the normalization is necessary at that
specialization; interpreting the resulting homogeneous equation
as selecting a unique state would lose information.

## 3. The characteristic equation and its original action

The characteristic polynomial of (5) is obtained by replacing
the shift \(a\mapsto a+1/N\) with a variable \(\lambda\) and
then setting \(r=1\). Put
\[
             d=X+(1-X)\lambda.
 \tag{12}
\]
Multiplication of the resulting symbol by \(X\) gives
\[
              (X-1)d^2+(W-X)d+X(1-W).
 \tag{13}
\]
This computation specifies a boundary characteristic polynomial;
it asserts no semiclassical approximation to the actual sum.

There is an exact match with the already proved conditional critical
equation on its original regular chart. Its normalized phase is
\[
 \mathscr F(s;a,y)=g(s+a)+g(s+y)-2g(s)-g(a)-g(y)+2\pi ias.
 \tag{14}
\]
Let \(s_*(a,y)\) be a simple critical point with its original zero
logarithmic lift, and set \(U=e^{-2\pi is_*}\). Stationarity gives
\[
                  (1-XU)(1-WU)=X(1-U)^2.
 \tag{15}
\]
For the critical action \(\Phi(a,y)=\mathscr F(s_*;a,y)\),
the chain-rule term involving \(\partial_a s_*\) vanishes. Hence
\[
 e^{\partial_a\Phi}
       =\frac{1-XU}{U(1-X)},\qquad
 X+(1-X)e^{\partial_a\Phi}=U^{-1}.
 \tag{16}
\]
Substitution of \(d=U^{-1}\) transforms (13) into (15), up to
its nonzero factor and overall sign. Both the incoming derivative
and the internal critical point therefore belong to the same
specified branch; no independent square-root choice was made.

At the constant shift \(\lambda=1\), the unmultiplied symbol is
\[
                         (W-1)(X^{-1}-1).
 \tag{17}
\]
It is nonzero on the actual incoming and outgoing parameter domains.
The forcing in (6) is unchanged by the shift \(X\mapsto rX\).
It must therefore be retained as a separate term; it cannot be
absorbed into a solution of the homogeneous characteristic equation.
Its vanishing on physical nodes also does not imply vanishing of
its parameter derivatives there.

The successful first-order argument for
[three negative crossings](research_mixed_fourier_negative_three_connection.md)
uses a polynomial bound on a specifically normalized holomorphic
current before applying Cauchy's estimate. Equation (6) alone supplies
no analogous bound or decomposition for \(F_N\). The full
twice-crossed asymptotic still requires control of the right contour,
the endpoint current, and their possible cancellation with the known
left-path contribution.
