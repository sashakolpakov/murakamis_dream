# Uniform real-row tails for the lower endpoint bridge

Research deduction, 7 November 2026. For the specified complete
endpoint coefficient, all auxiliary rows outside a moving regular
interval reduce to its two real cuts and one explicit upper-half
ceiling on a larger negative-height strip. In particular every
off-grid row revived beyond the private endpoint is retained.

This proves a finite-source tail estimate. It does not locate the
continued cap saddle in this strip, compare the real cuts with its
critical action, pay the retained contour aliases, or assert a
complete endpoint packet on the strip. No numerical evaluation is
used, and earlier frozen notes are unchanged.

## 1. The original complete source and the new strip

Keep the finite continuation of
[the complex-index endpoint theorem](research_complete_boundary_complex_index.md):
\[
 \begin{split}
 C_N(e,w)&=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\\
 S_l&=\prod_{j=1}^{l}2\sin(\pi j/N),\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu .
 \end{split}                                                    \tag{1}
\]
The canonical factorial, complete Newton polynomials, and original
primitive branches are unchanged. At \(e=j/N\), the terms \(l>j\)
vanish by the reciprocal-factorial zeros; the finite definition
in (1) never deletes those terms at a nonphysical \(e\).

Write \(e=E-i\eta\), and consider
\[
 \mathcal E_{\rm tail}=
 \left\{\frac6{25}\le E\le\frac{49}{100},\quad
                               0\le\eta\le\frac3{50}\right\}.
                                                                  \tag{2}
\]
The real proof cuts are
\[
                 a=\frac1{20},\qquad b(E)=E-\frac1{100}.
                                                                  \tag{3}
\]
Thus \(23/100\le b(E)\le12/25\), and the arguments of \(F\)
are regular on the real interval \([a,b(E)]\). These cuts split
the proof of one fixed finite function; they do not define a
new interpolation.

For \(0\le x\le1\), use the original zero-safe row upper rate
\[
 \begin{split}
 \mathcal V(x)&=2\int_0^x\log(2|\cos\pi s|)\,ds-2J(x),\\
 R(e,x)&=\mathcal V(x)-J(x)-\Re J_{\rm side}(e-x)+\pi\eta x .
 \end{split}                                                    \tag{4}
\]
Here \(J_{\rm side}\) is precisely the reflected reciprocal-factorial
primitive in Sections 3--4 of the complex-index theorem.
Every literal summand of (1), and each fixed ordinary-color
derivative at \(w=-2\), has modulus at most
\(N^C e^{NR(e,l/N)}\). This includes the odd Newton zero and
the negative-integer reciprocal zeros, with the original
polynomial errors. The carrier \(+\pi\eta x\) in (4) is retained.

**Theorem.** Uniformly on (2),
\[
 \begin{array}{ll}
 R(e,x)\le\Re F(e,a),&0\le x\le a,\\[1mm]
 R(e,x)\le\Re F(e,b(E)),&b(E)\le x\le1/2,\\[1mm]
 R(e,x)<67/105,&1/2\le x\le1.
 \end{array}                                                     \tag{5}
\]
More precisely, where its derivative is finite,
\[
 e^{\partial_xR(e,x)}>27\quad(0<x\le a),\qquad
 e^{\partial_xR(e,x)}<
                 \frac{2569}{3375}<\frac45
                        \quad(b(E)\le x<1/2).                 \tag{6}
\]
The inequalities extend across integrable logarithmic zeros
by continuity and integration. No condition on the sign of the
auxiliary critical height is used.

## 2. The lower real rows

The exact derivative of the rate, on either reflected side, is
\[
 e^{\partial_xR(e,x)}
  =e^{\pi\eta}
       \frac{|\sin\pi(e-x)|\cos^2(\pi x)}
                              {\sin^3(\pi x)}
                       \qquad(0<x<1/2).                      \tag{7}
\]
For \(0<x\le1/20\), one has
\[
 19/100\le E-x<1/2,\qquad
 |\sin\pi(e-x)|>\frac12,\quad
 \cos^2\pi x>\frac14,\quad
                         \sin\pi x<\frac16 .
 \]
The first sine bound follows from \(19/100>1/6\), and the
others from \(x\le1/20\), \(\pi<10/3\). Since
\(e^{\pi\eta}\ge1\), (7) is greater than \(27\).
At the cut \(a<E\), \(R(e,a)=\Re F(e,a)\). Integration
proves the first line of (5), including the actual row \(l=0\).

## 3. Every upper row below one half, including the revived rows

For \(b(E)\le x<1/2\), put
\[
             z=\cot\pi x,\quad S=\sin\pi E,\quad
             C=\cos\pi E,\quad K=\sinh(\pi\eta).
 \]
All these quantities except possibly \(z,K\) are positive.
The following elementary bounds hold throughout the domain:
\[
       0\le z<\frac65,\qquad S>\frac23,\qquad
       C<\frac34,\qquad K<\frac15,\qquad
                                 e^{\pi\eta}<\frac54.          \tag{8}
\]
Here \(x\ge23/100\), so \(\pi x>23/32\) by \(\pi>25/8\).
The positive tangent lower bound gives
\[
 \tan(\pi x)>
 \frac{23}{32}+\frac{(23/32)^3}{3}
                 =\frac{82823}{98304}>\frac56,
 \]
proving the bound for \(z\). Since \(\pi E>3/4\),
\(\sin(3/4)\ge3/4-(3/4)^3/6>2/3\) proves the bound for \(S\).
The cosine upper polynomial at \(3/4\) gives
\[
 \cos(3/4)\le1-\frac{(3/4)^2}{2}+\frac{(3/4)^4}{24}
                                                  <\frac34,
 \]
proving the bound for \(C\).

For the height, \(\pi\eta\le3\pi/50<19/100\).
The positive series gives
\[
 \sinh t\le\frac{t}{1-t^2/6}\quad(0\le t<\sqrt6);
 \]
at \(t=19/100\), the inequality
\(5t+t^2/6<1\) shows this is less than \(1/5\).
Finally
\[
 \pi\eta<\frac15<\frac29<\log(5/4)
 \]
by \(\log(1+s)>2s/(2+s)\) at \(s=1/4\).
This proves all of (8).

The exact sine modulus in (7) yields
\[
 e^{\partial_xR(e,x)}
 =e^{\pi\eta}z^2
       \sqrt{(Sz-C)^2+K^2(1+z^2)}
 \le e^{\pi\eta}
       \{z^2|Sz-C|+Kz^2\sqrt{1+z^2}\}.                       \tag{9}
\]
The real-angle term must be bounded on both sides of \(x=E\).
For \(x\ge E\), one has \(0\le z\le C/S\), and the elementary
maximum of \(z^2(C-Sz)\) on this interval is
\[
                 \frac{4C^3}{27S^2}<\frac9{64}
                                                  <\frac4{27}. \tag{10}
\]
The middle bound follows directly from \(C<3/4,S>2/3\).
For \(b(E)\le x\le E\), the original trigonometric expression
instead gives
\[
 z^2|Sz-C|
    =\frac{\sin\pi(E-x)\cos^2\pi x}{\sin^3\pi x}
    <\frac{4/125}{(3/5)^3}=\frac4{27}.                        \tag{11}
\]
Indeed \(0\le E-x\le1/100\), so the numerator is at most
\(\pi/100<4/125\). Also
\[
 \sin\pi x>\sin(23/32)
                  \ge\frac{23}{32}-\frac{(23/32)^3}{6}
                                                   >\frac35 .
 \]
Thus (11) includes the entire short interval before the reflected
wall. At \(x=E,\eta=0\), the exact rate derivative can be
minus infinity; its continuous integral still has the asserted
monotonicity.

For the height term in (9), (8) and \(\sqrt{61}<8\) give
\[
       Kz^2\sqrt{1+z^2}
                 <\frac15\,\frac{36}{25}\,\frac85
                                           =\frac{288}{625}. \tag{12}
\]
Combining (8)--(12) proves
\[
 e^{\partial_xR(e,x)}
  <\frac54\left(\frac4{27}+\frac{288}{625}\right)
                    =\frac{2569}{3375}<\frac45.              \tag{13}
\]
The difference in the last comparison is \(131/3375>0\).
The rate therefore decreases from the actual regular cut
\(b(E)<E\) through all revived rows \(x>E\) up to \(1/2\).
Since \(R(e,b(E))=\Re F(e,b(E))\), this proves the second
line of (5).

## 4. The complete upper half

The reflection identity in
[the endpoint extension proof, Lemma 1](research_mixed_endpoint_packet_extension_criterion.md)
is valid on the present strip as well. Its proof uses only
\(1/6<E<1/2\), not its former stronger lower real bound.
Writing \(v=1-x\), it reads
\[
 R(e,1-v)=2J(1/2-v)+3J(v)-\Re J(e+v)
                                    +\pi\eta+\pi(1-v)\eta .
                                                                  \tag{14}
\]
The first two terms are nonpositive. Before \(\Re(e+v)\)
reaches \(1/2\), the horizontal derivative of \(\Re J(e+v)\)
is positive, because \(E>1/6\). Above \(1/2\), the original
vertical comparison gives \(\Re J(e+v)\ge0\), whereas
\(\Re J(e)\le J(E)<0\). Hence
\[
             R(e,x)\le-\Re J(e)+2\pi\eta
                          \qquad(1/2\le x\le1).              \tag{15}
\]
On \(0<E<1/2\), the sine argument has modulus less than
\(\pi/2\). Its vertical integral therefore gives
\[
              -\Re J(E-i\eta)\le-J(E)+\pi\eta/2
                                         <1/6+\pi\eta/2.     \tag{16}
\]
The established elementary inequality
\(\max_{0\le E\le1/2}(-J(E))<1/6\) is the same one used
in the complex-index theorem. Now \(\eta\le3/50\) and
\(\pi<22/7\) imply
\[
 R(e,x)<\frac16+\frac{5\pi\eta}{2}
                  \le\frac16+\frac{3\pi}{20}
                  <\frac{67}{105}.                          \tag{17}
\]
This includes the true upper endpoint by continuity. No
physical-grid vanishing of a revived row is used.

## 5. Finite cut conventions and exact scope

For a base parameter \(e=E-i\eta\), let
\[
 L_N=\lceil Na\rceil,\qquad M_N(E)=\lceil Nb(E)\rceil,\qquad
 a_N=(L_N-1/2)/N,\quad b_N=(M_N(E)-1/2)/N .                  \tag{18}
\]
Only \(L_N\le l<M_N(E)\) will be represented by a retained
contour; the present theorem makes no assertion about that
contour. Every other literal summand remains in its complete
finite tail. Equations (4)--(5) and the uniform zero-safe
factorial bounds show, for each fixed ordinary derivative
order \(k\) at \(-2\) and every \(\tau>0\),
\[
 \begin{split}
 &\sum_{\substack{0\le l<N\\ l<L_N\ {\rm or}\ l\ge M_N(E)}}
 \left|
 \frac{e^{i\pi e l}e_l^{(k)}(-2)}
                    {S_lG_N(Ne-l)}
 \right|\\
 &\quad\le C_{\tau,k}N^{A_{\tau,k}}
 \left[
  e^{N(\Re F(e,a)+\tau)}
  +e^{N(\Re F(e,b(E))+\tau)}
  +e^{N(67/105+\tau)}
 \right].
 \end{split}                                                  \tag{19}
\]
The \(O(N^{-1})\) half-grid shifts in (18) are absorbed by
the continuous zero-safe rates and their original
\(O(\log N)\) factorial errors. Equation (19) retains the
full source normalization (1), its carrier, both level
parities, and every reciprocal zero. It does not divide
by a sampled coefficient.

On a sufficiently small fixed ordinary-color neighborhood
of \(-2\), the original uniform Newton product upper bound
gives the same assertion with the chosen extra tolerance.
For outside-parameter derivatives, first fix a base
decomposition (18); do not differentiate its floor or ceiling.
Its row sets are then fixed finite holomorphic sums.
The continuous reflected upper rates preserve (19), with
an arbitrarily small additional allowance, on sufficiently
small fixed complex neighborhoods. Cauchy's formula gives
all fixed derivatives there. No derivative of a moving
cutoff is being asserted.

To obtain a complete packet from these bounds one must
still prove the actual original critical point lies between
the retained cuts, compare both real cuts and \(67/105\)
with its critical action, and pay every horizontal alias,
vertical side and unweighted joining current. One must
also establish that any proposed actual cap path lies
in the domain (2). Those assertions are not consequences
of (19), and are not made here.
