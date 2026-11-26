# The complete lower-output conditional source reduced to its real middle integral

Research deduction, 8 November 2026. The original conditional
sum at negative outgoing height is reduced to one retained real
integral. Both physical ends and all six weighted cotangent
currents are exponentially smaller after multiplication by the
complete first cap and the actual ordinary-next factors. The
unweighted deformation of the retained integral is not asserted.
An accompanying algebraic root and curvature bound identifies a
fixed regular height strip available for that remaining problem.

No numerical evaluation or frozen-source edit is used.

## 1. Original source, cuts, and the continuous two-branch upper rate

Keep the incoming rectangle and finite factors of
[the upper-block theorem](research_mixed_conditional_lower_output_upper_block.md):
\[
 a=x-i\eta,\quad \frac12\le x\le\frac7{10},\quad
 0\le\eta\le\frac9{125},\qquad X=e^{-2\pi ia}.
 \]
For the contour estimates one may take
\[
 y=z-i\xi,\quad \frac{11}{50}\le z\le\frac9{20},\quad
                     0\le\xi\le\frac{27}{250},
             \qquad Y=e^{-2\pi iy}.
                                                               \tag{1}
\]
The actual next-source comparison below uses only
\(y\in P+i\Im y_*\), with \(-.102<\Im y_*<-.001\),
and its original independent outgoing plateau.

Use the literal finite source and fixed integer cuts
\[
 \begin{split}
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
              \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 L_N&=\lfloor2N/25\rfloor+1,\qquad M_N=\lceil N/2\rceil,\\
 \ell_N&=(L_N-\tfrac12)/N,\qquad
 b_N=(M_N-\tfrac12)/N .
 \end{split}                                                    \tag{2}
\]
For all sufficiently large \(N\), \(3/40<\ell_N<b_N\le1/2\).
The retained rows are exactly \(L_N\le j<M_N\).

The canonical interpolant is the original holomorphic function
\[
 T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3 .
                                                               \tag{3}
\]
At \(s=j/N\), it equals the corresponding summand in (2).
The original chirp has not been removed.

The exact factorial identity and zero-safe estimate from
[the half-cut proof, Section 2](research_mixed_conditional_half_cut_below_incoming_zero.md)
and [complete nonnegative-height continuation, Section 2](research_mixed_conditional_nonnegative_height_complete_source.md)
give the following continuous upper rate. Define
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi(\Im q)_+,&1\le\Re q<2.
 \end{cases}
                                                               \tag{4}
\]
The boundary values agree continuously. For \(s=t+i\sigma\),
\[
 \widehat R(t,\sigma)=
 \mathfrak p(a+s)+
 \Re\{g(y+s)-3g(s)-g(a)-g(y)+2\pi ias\}.
                                                               \tag{5}
\]
Uniformly on the closed rectangle
\(\ell_N\le t\le b_N,\ |\sigma|\le2\),
\[
                  |T_N(s;a,y)|
       \le C_\tau N^{A_\tau}e^{N(\widehat R(t,\sigma)+\tau)} .
                                                               \tag{6}
\]
The only numerator that may leave its first real strip is
\(\Pi_N(a+s)\). The original identity
\(\Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q)\)
keeps both its terms and produces the last term of (4).
At approach to the zero line, the exact reflected factorial
identity and the reciprocal midpoint bound cited in the half-cut
proof give the same one-sided upper estimate. This includes the
odd half cut and the even half cut approaching it. No division
by \(1-e^{-2\pi iNa}\) is made.

All other real arguments stay in fixed regular strips:
\(0<t<1\), \(0<\Re(y+s)<1\), and \(0<\Re a,\Re y<1\).
Their bounded heights in (1) and \(|\sigma|\le2\) lie in the
original compact-height factorial domains. Thus lowering the
outgoing height introduces no new interpolation pole or branch
in (3)--(6). At \(\sigma=0\), (5) is exactly the original
absolute physical-row rate, including after the real incoming
numerator wall.

## 2. All weighted vertical sides still decay

Put \(A(q)=\Arg(1-e^{-2\pi iq})\), with its original strip
argument. On the part \(x+t<1\), direct differentiation gives
\[
 \partial_\sigma\widehat R
   =-A(a+s)-A(y+s)+3A(s)-2\pi x.
                                                               \tag{7}
\]
For \(\sigma\ge0\), use the same original argument bounds as
in [the lower-current proof](research_mixed_conditional_negative_height_lower_currents.md):
\[
 \partial_\sigma\widehat R
 \le2\pi-4\pi t+\max\{2\pi(z+t)-\pi,0\}\le9\pi/5 .
                                                               \tag{8}
\]
The last inequality uses \(t\ge3/40\) and \(z\le9/20\).
It has no outgoing-height assumption.

For \(\sigma\le0\), the outgoing radius at \(y+s\) is at
most one. If \(z+t<1/2\), then
\[
 A(y+s)\le\pi/2-\pi(z+t)<\pi/4
 \]
because \(z+t>11/50+3/40>1/4\). If \(z+t\ge1/2\), that
argument is nonpositive. The incoming argument in (7) is
nonpositive, and the own argument is nonnegative. Consequently
\[
                  \partial_\sigma\widehat R\ge-33\pi/20 .
                                                               \tag{9}
\]
This is the previous lower slope, now with an easier outgoing
radial bound.

For \(x+t\ge1\), write \(r_0=x+t-1\in[0,1/5]\).
The exact two-branch derivative is
\[
 \begin{split}
 \partial_\sigma\widehat R={}&
 -A(r_0+i(\sigma-\eta))-A(y+t+i\sigma)
   +3A(t+i\sigma)-2\pi x\\
 &\hspace{30mm}+2\pi{\bf1}_{\{\sigma>\eta\}} .
 \end{split}                                                    \tag{10}
\]
Take the one-sided limits at \(r_0=0\); the rate remains
continuous. Here \(z+t>1/2\), so the outgoing argument is
nonpositive at every height.

For \(0\le\sigma\le\eta\), its incoming argument is
nonnegative. The bounds
\(A(y+s)\ge\pi-2\pi(z+t)\) and
\(A(s)\le\pi-2\pi t\) yield
\[
 \partial_\sigma\widehat R
       \le\pi(2+2z-4t-2x)\le3\pi/10 .
 \]
For \(\sigma\ge\eta\), the incoming argument is at least
\(\pi/2-\pi r_0\), hence
\[
 \partial_\sigma\widehat R
       \le\pi(5/2-x-3t+2z)\le9\pi/5.
                                                               \tag{11}
\]
Both last inequalities use \(t\ge1-x\).

For \(\sigma\le0\), the incoming radius is at most one
and its argument is at most \(\pi/2-\pi r_0\).
The own and negative-outgoing contributions in (10) are
nonnegative. Thus
\[
 \partial_\sigma\widehat R\ge-19\pi/10 .
 \]
If \(\sigma\le-1/8\), its incoming radius is less than
\(e^{-\pi/4}<1/2\), so that argument is at most \(\pi/6\).
Therefore
\[
 \partial_\sigma\widehat R\ge-47\pi/30
                         \qquad(\sigma\le-1/8).
                                                               \tag{12}
\]
These are exactly the full-side bounds of the half-cut proof,
with the outgoing-height dependence checked explicitly.
They integrate through the finite kink in (4).

On either half-grid vertical line in (2), the appropriate
cotangent remainder is bounded by
\(2e^{-2\pi N|\sigma|}\). Equations (8)--(12) therefore
bound both upper vertical remainders by their real-cut rate
minus \(\pi\sigma/5\); the lower ones lose at least
\(\pi|\sigma|/10\). In the prewall part the lower loss is
the stronger \(7\pi|\sigma|/20\).

The real lower cut is paid by
[the complete low-block proof, Section 3](research_mixed_conditional_lower_output_low_block.md).
The real upper cut is paid by the continuous upper-row rate
of the upper-block theorem and uniform continuity of (5).
Indeed \(b_N\to1/2\); a fixed real collar shares its strict
joint source reserve, including at the continuous incoming
wall. Consequently all four complete weighted vertical
half-sides are paid after multiplication by the original
cap, weight, and ordinary-next factor.

## 3. Both horizontal remainders

The elementary exact-carrier estimate in the low-block proof,
and \(|Y|\le1\), give throughout \(0<t\le1/2\)
\[
 \widehat R(t,0)<\frac{17}{10}t-3J(t)<\frac{27}{20}.
                                                               \tag{13}
\]
Here \(-J(t)<1/6\) is the original uniform sine-factorial
bound. This is a positive real-row bound, not a statement
about a chosen saddle.

At height \(+2\), the upper slope \(9\pi/5\) and the
cotangent loss \(2\pi|\sigma|\) leave a loss \(2\pi/5\).
At height \(-2\), the prewall loss is \(7\pi/10\).
For the postwall part, the two ranges in (12) give
\[
 \frac{\pi}{10}\frac18+
       \frac{13\pi}{30}\frac{15}{8}
                      =\frac{33\pi}{40}>\frac{7\pi}{10}.
 \]
The horizontal kernels have the same bound with a factor
four instead of two. Thus each horizontal remainder, before
the complete cap is inserted, has rate at most
\[
                         \frac{27}{20}-\frac{2\pi}{5}.
 \]
Using the complete cap rate \(1549/1500\) and \(\pi>25/8\),
their joint prefix rate is strictly below
\[
       \frac{1549}{1500}+\frac{27}{20}-\frac54
                    =\frac{1699}{1500}<\frac{25}{16}.
                                                               \tag{14}
\]
The original unselected marginal comparison in the upper-block
theorem therefore pays both complete horizontal sides, with
the next weight's forcing term and the full third kernel retained.

## 4. Exact real-integral reduction and its actual error

Apply the original split cotangent identity at heights \(\pm2\):
\[
 \begin{split}
 \sum_{j=L_N}^{M_N-1}T_N(j/N)
    &=N\int_{\ell_N}^{b_N}T_N(t)\,dt+\mathcal R_N,\\
 \mathcal R_N&=\frac{N}{2i}\left\{
   \int_{\partial R^+}T_N(s)[\cot(\pi Ns)+i]\,ds+
   \int_{\partial R^-}T_N(s)[\cot(\pi Ns)-i]\,ds\right\}.
 \end{split}                                                    \tag{15}
\]
Each sign-half boundary omits its real segment and retains its
original induced orientation. These are the four vertical
half-sides and two horizontal sides estimated above. The
interpolant (3) remains holomorphic across the incoming
numerator wall. Its zeros cause no extra residue.

Define the exact remainder
\[
 \mathcal E_N=C^{\rm lo}_{1,N}+C^{\rm up}_{1,N}
                                      +\mathcal R_N .
 \]
Then the original finite kernel obeys
\[
             C_{1,N}(X,Y)
        =N\int_{\ell_N}^{b_N}T_N(t;a,y)\,dt+\mathcal E_N .
                                                               \tag{16}
\]
No phase replacement has entered this identity.

For the actual ordinary-next references and independent
unselected/output plateaux of the two block theorems, the
complete source error has the bound
\[
 \begin{split}
 &|U_{0,N}(w,X)\mathcal E_N(a,y)
                    d_N(Y)C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
          e^{N\{\Lambda_{123}(z_{\rm out})-1/100+\tau\}},
                  \qquad\beta=0,1,\quad w\in[-2,2].
 \end{split}                                                    \tag{17}
\]
The variable \(z_{\rm out}\) here is the third continuous
leg; the \(z\) in (1) is the real part of \(y\).
The low and upper block gaps are respectively greater than
\(1/50\) and \(1/25\). The weighted sides preserve the
corresponding real-cut gaps, after the uniform \(O(1/N)\)
cut displacements and the arbitrary finite tolerances.
The horizontal gaps follow from (14). Sharing these reserves
gives (17).

At the actual outgoing reference and on sufficiently small
fixed neighborhoods, the original nonzero outgoing factorial
packet removes the halfweight when \(\beta=1\), exactly as
in the block theorems. With the original first and next
measures \(N\,da\) and \(N\,dy\), the normalized integrated
error and every fixed mixed jet have gap \(1/400\).
The paths and integer cuts are fixed at the base reference
before outside parameters vary. Uniform zero-safe rates on
all the closed currents give a fixed complex neighborhood;
Cauchy's formula on a smaller one gives the stated jets.
Both level parities and all real ordinary-color bounds remain.

## 5. A regular height strip for the remaining critical equation

The following written bounds concern the original phase only;
they do not estimate the real integral in (16).
For the parameters (1),
\(\Re X<0,\Im X\ge0,5/8<|X|\le1\), and
\(\Im Y<0,\Re Y<1,|Y|\le1\).
In particular \(3|X|^2>1\), so these parameters belong to
[the algebraic transport domain](research_mixed_four_conditional_algebraic_transport_domain.md).
Its unique upper root is simple and has the original zero lift:
\[
 \begin{gathered}
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0,\qquad
 t_*=\frac{\Log v}{2\pi i},\\
 Q_t(t_*;a,y)=0,\qquad0<\Re t_*<1-x .
 \end{gathered}                                                 \tag{18}
\]

All roots of this cubic satisfy
\[
                         \frac15<|v|<5.
                                                               \tag{19}
\]
For the upper bound, \(|1-X|\ge1\) and the other three
coefficient moduli are at most \(3,4,1\); the elementary
monic Cauchy bound gives \(1+\max\{3,4,1\}=5\).
Equality at radius five is excluded by the strict finite
geometric-sum inequality in its usual proof.
For the reciprocal polynomial, division by \(X\) gives
\[
 w^3+(Y-3)w^2+(2-Y/X)w+(1/X-1).
 \]
Its nonleading coefficients have moduli at most
\(4,18/5,13/5\), respectively. The same bound gives
\(|w|<5\). Since \(X\ne0\), no original root is zero.
Thus
\[
                       |\Im t_*|\le\frac{\log5}{2\pi}.
                                                               \tag{20}
\]

The selected root also satisfies
\[
                  |v|<2,\qquad \Re t_*>\frac2{25}.
                                                               \tag{20a}
\]
For the first assertion, if \(|v|\ge2\), each of
\(\Log(1-X/v)\), \(\Log(1-Y/v)\), and \(\Log(1-1/v)\)
has argument of modulus at most \(\pi/6\). These are
the original strip logarithms. Since the last occurs with
multiplicity three,
\(\Im Q_t\ge2\pi x-5\pi/6\ge\pi/6>0\), contradicting
the zero lift in (18).

To prove the second assertion, suppose \(u=\Re t_*\le2/25\),
put \(\theta=2\pi u\), \(U=e^{2\pi\Im t_*}=1/|v|>1/2\),
and retain \(T=e^{2\pi\eta}\ge1\). If \(U\ge8/5\), the
own argument satisfies
\[
 \Arg(1-Ue^{-i\theta})
  \ge\pi-\theta-\arcsin(5/8)
  >\pi-\theta-7\pi/30 .
 \]
Indeed
\(\sin(7\pi/30)>\sin(7/10)>7/10-(7/10)^3/6>5/8\).
The incoming argument is nonpositive since
\(x+u\in[1/2,39/50]\). The outgoing argument is at most
\(14\pi/25-\theta\): for \(z+u<1/2\) this is the
original strip bound \(\pi-2\pi(z+u)\), and otherwise
the argument is nonpositive. Hence
\[
 \Im Q_t<
 \frac{7\pi}{5}+\frac{14\pi}{25}-\theta
           -3(\pi-\theta-7\pi/30)
 \le-\frac{\pi}{50}<0.
 \]
This again contradicts (18), so \(1/2<U<8/5\).

In that remaining range the exact chirp-folded force is
\[
 |e^{Q_t}|^2=
 \frac{|T-Ue^{-2\pi i(x+u)}|^2
       |1-RUe^{-2\pi i(z+u)}|^2}
      {|1-Ue^{-i\theta}|^6},\qquad R=|Y|\le1 .
                                                               \tag{20b}
\]
Both cosines in its numerator are less than \(1/5\), since
\(x+u\in[.5,.78]\) and \(z+u\in[.22,.53]\).
This follows from \(\sin(3\pi/50)<1/5\).
The first squared modulus is increasing in \(T\ge1\)
after this replacement, and is greater than
\(1+U^2-2U/5>1\). The second is greater than \(24/25\)
by completion of the square in \(RU\).
Also \(\cos\theta>6/7\), and convexity in \(U\) gives
\[
 |1-Ue^{-i\theta}|^2
 <1+U^2-\frac{12U}{7}
 \le\max\left\{\frac{11}{28},\frac{143}{175}\right\}
                  <\frac56.
                                                               \tag{20c}
\]
The cosine bound follows from the elementary left-endpoint
estimate used below. Equation (20b) is therefore greater
than \((24/25)/(5/6)^3>1\), contradicting \(Q_t=0\).
This proves (20a) without an action evaluation.

There is strict horizontal phase concavity on the prewall strip
\[
 \frac2{25}\le u<1-x,\qquad
                    |\sigma|\le\frac{\log5}{2\pi},
                        \qquad s=u+i\sigma .
                                                               \tag{21}
\]
Write \(C(q)=\Re\cot(\pi q)\). Then
\[
 \Re Q_{ss}=\pi\{C(a+s)+C(y+s)-3C(s)\}.
                                                               \tag{22}
\]
The incoming term is negative on the strict prewall strip.
If \(u+z\ge1/2\), the outgoing term is nonpositive and
\(C(s)>0\), proving the assertion directly.

If \(u+z<1/2\), then \(u<7/25\). Put
\(\theta=2\pi u\), \(A=\cosh(2\pi\sigma)\le13/5\).
Here
\[
 \frac{4\pi}{25}\le\theta<\frac{14\pi}{25},\qquad
 \frac1{C(s)}=\frac{A-\cos\theta}{\sin\theta}.
 \]
The derivative of the last expression is
\((1-A\cos\theta)/\sin^2\theta\), so it has no interior
maximum. At the left endpoint, the elementary bounds
\[
 \sin(4\pi/25)>\sin(1/2)>23/48>19/40,\qquad
 \cos(4\pi/25)>193/225>6/7
 \]
follow from \(1/2<4\pi/25<8/15\) and the usual sine and
cosine Taylor inequalities. At the right endpoint,
\(3\pi/50<1/5\) gives
\(\cos(14\pi/25)>-1/5\) and
\(\sin(14\pi/25)>49/50>9/10\). Consequently
\[
 \frac1{C(s)}<
 \max\left\{\frac{13/5-6/7}{19/40},
             \frac{13/5+1/5}{9/10}\right\}
       =\max\{488/133,28/9\}=\frac{488}{133}.
                                                               \tag{23}
\]
For the outgoing term, \(2\pi(u+z)\ge3\pi/5\), and its
cosine is at most
\((1-\sqrt5)/4<-1/4\). Its sine is at most one and
its hyperbolic denominator is at least \(1-\cos(2\pi(u+z))\).
Thus \(C(y+s)<4/5\), for every outgoing imaginary part.
Substituting in (22) yields the explicit bound in this case:
\[
                  \Re Q_{ss}<-\frac{43\pi}{2440}.
                                                               \tag{24}
\]
In the other case the already proved strict sign is uniform
on each compact strict prewall substrip. No global numerical
constant is assigned there.

Equations (18)--(24) place the critical point strictly inside
the retained prewall height strip. Compactness gives a uniform
separation from the lower cut, the real incoming wall, and the
primitive divisors on the actual parameter family. These phase
statements do not pay an unweighted connector or compare the
critical action with the following source plane.
The retained real integral in (16), including every wall row,
is the remaining finite-source obligation. A future deformation
must keep both unweighted sides and the complete original
amplitude. No whole next-transfer asymptotic or terminal
family claim follows from the present reduction.
