# Initial incoming rows when the next coordinate approaches one half

Research proof, 8 November 2026. This note supplies the physical-row
and factorial-boundary estimates needed to extend the initial real
incoming segment to a second coordinate with real part between
\(9/20\) and \(1/2\). It uses the original finite kernels throughout.
No numerical evaluation is used.

The results below do not by themselves estimate the entire next
transfer. The central contour profiles at the incoming endpoint
\(a=1/10\), and the following conditional kernel, must still have
their required bounds. The point here is that the physical rows,
the small initial collar and the first numerator zero introduce
no additional obstruction to that extension.

## 1. Every upper physical row reduces to the half or last row

Put \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}.
 \tag{1}
\]
In this section take
\[
 0\le x\le\frac1{10},\qquad \frac9{20}\le q\le\frac12,
 \qquad \frac12\le R\le1,\qquad
 X=e^{-2\pi ix},\quad Y=Re^{-2\pi iq}.
 \tag{2}
\]
In particular the actual radii \(R=e^{2\pi h_y}\), with
\(-.102<h_y<-.001\), lie in (2). Indeed
\(.204\pi<2/3<\log2\).

Define the continuous real primitives
\[
 f_R(s)=\log|1-Re^{-2\pi is}|,\qquad
 J(t)=\int_0^t f_1(s)\,ds,
\]
and the real rate of the original row by
\[
 E(t;x,q,R)=
 \int_0^t f_1(x+s)\,ds+
 \int_0^t f_R(q+s)\,ds-3J(t),\qquad 0\le t\le1.
 \tag{3}
\]
All logarithmic zeros in these integrals are integrable.
The inverse power \(X^{-j}\) has modulus one. The mean of each
numerator logarithm over one period is zero, including \(R=1\).
For \(R<1\) this follows by integrating the convergent series for
\(\log(1-Re^{-2\pi is})\); passage to \(R=1\) follows by integrable
convergence. Consequently \(E(1)=0\).

**Lemma 1.** Uniformly in (2),
\[
 \max_{1/2\le t\le1}E(t;x,q,R)
             =\max\{E(1/2;x,q,R),0\}.
 \tag{4}
\]

**Proof.** Set \(v=1-t\). Reflection across the full period gives
\[
 \mathscr F(v):=E(1-v)
 =-\int_{x-v}^{x}f_1(s)\,ds
  -\int_{q-v}^{q}f_R(s)\,ds+3J(v).
 \tag{5}
\]
We first prove \(\mathscr F(v)<0\) for \(0<v\le9/40\).
Every point of the second integration interval then lies in
\([9/40,1/2]\). Hence
\[
 2\cos(2\pi s)\le2\sin(\pi/20)<\pi/10<1/2\le R,
\]
and
\[
 |1-Re^{-2\pi is}|^2
       =1+R\{R-2\cos(2\pi s)\}>1.
\]
Thus its logarithmic integral is positive.
Among intervals of length \(v\le1/2\), the integral of \(f_1\)
is minimized by an interval centered at an integer. This follows
by moving its endpoints toward that integer, since \(f_1\)
increases with distance from the integers up to distance \(1/2\).
The first integral in (5) is therefore at least \(2J(v/2)\).
Using \(\sin(\pi s)\le\pi s\), we obtain
\[
\begin{split}
 \mathscr F(v)
 &\le 3J(v)-2J(v/2)\\
 &=J(v)+2\int_{v/2}^{v}\log(2\sin\pi s)\,ds\\
 &\le v\{\log(2\pi v)-1\}
       +v\{\log(4\pi v)-1\}\\
 &=v\{\log(8\pi^2v^2)-2\}<0.
\end{split}
 \tag{6}
\]
For the last inequality it is enough that \(v\le1/4\),
\(\pi^2<10\) and \(e^2>5\).

For \(9/40\le v\le1/2\), write \(S(v)=2\sin\pi v\).
Here \(0\le v-x\le v\le1/2\), so the first endpoint modulus
in (5) is at most \(S(v)\). Differentiation away from its zeros gives
\[
 \exp\mathscr F'(v)
 =\frac{S(v)^3}
 {|1-e^{-2\pi i(x-v)}|\,|1-Re^{-2\pi i(q-v)}|}
 \ge\frac{S(v)^2}{|1-Re^{-2\pi i(q-v)}|}.
 \tag{7}
\]
The last quotient is strictly greater than one:

* If \(9/40\le v\le1/4\), then \(1/5\le q-v\le11/40\).
  Convexity of \(|1-Re^{-2\pi is}|^2\) in \(R\in[0,1]\)
  gives an upper bound \(\max\{1,2|\sin\pi s|\}\) for its modulus.
  Consequently the denominator of (7) is at most
  \(2\sin(11\pi/40)\), whose square is
  \(2+2\sin(\pi/20)<2+\pi/10<64/25\).
  In contrast,
  \[
   S(v)^2\ge2-2\sin(\pi/20)>2-\pi/10>59/35>8/5.
  \]
* If \(1/4\le v\le1/3\), then \(0\le q-v\le1/4\).
  The denominator is at most \(\sqrt2\), while \(S(v)^2\ge2\).
* If \(1/3\le v\le1/2\), the denominator is at most two,
  while \(S(v)^2\ge3\).

The rational comparisons use only \(\pi<22/7\).
The derivative inequalities integrate through any numerator zeros,
because their logarithmic singularities are integrable.
Thus \(\mathscr F\) is increasing on \([9/40,1/2]\).
Together with (6) and \(\mathscr F(0)=0\), this proves (4).
\(\square\)

For every \(\epsilon>0\), the lemma yields the finite estimate
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}
 \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
 \le C_\epsilon N^{B_\epsilon}
   e^{N\{\max(E(1/2),0)+\epsilon\}},
 \tag{8}
\]
uniformly in (2), at both parities.
To justify uniformity even at moving numerator zeros, replace each
numerator logarithm by its maximum with a fixed negative cutoff.
These continuous functions have uniform Riemann-sum convergence on
the compact parameter set. Their integral error tends uniformly to
zero as the cutoff is removed: the only possible singularity is the
integrable logarithm of distance from a root, with \(R\ge1/2\).
The sine-factorial denominators have their original endpoint-uniform
estimate with \(O(\log N)\) error. Apply (4), then sum at most \(N\)
rows. This proves (8) without a lower bound for a numerator that
can vanish.

## 2. The lower physical rows and the small initial collar

For \(0<t\le11/100\), (2) gives
\[
 e^{\partial_tE(t)}
 =\frac{2\sin\pi(x+t)\,|1-Re^{-2\pi i(q+t)}|}
        {(2\sin\pi t)^3}>1.
 \tag{9}
\]
Indeed \(t\le x+t\le.21<1/2\), while
\(.45\le q+t\le.61\) makes the second numerator modulus
strictly greater than one. Thus all lower physical rows reduce
to their real cut \(t=11/100\), with the zero row retained.
The same upper Riemann-sum argument as above gives the uniform
finite version.

For the cap, keep the entire coherent functions in
\[
 U_{0,N}(w,X)=\sum_{e=0}^{N-1}
                  H_N(w,r^{-e})\,p_e(X)/P_e.
 \tag{10}
\]
The whole-coefficient and disk estimates of
[the seam theorem, Section 3](research_mixed_next_complete_source_seam_collar.md)
give, with arbitrarily small fixed tolerance,
\[
 \sum_e|H_N(w,r^{-e})|\le C_\tau N^B e^{N(101/125+\tau)},
 \qquad
 \sup_{|Y|\le1}\sum_j\frac{|p_j(Y)|}{|P_j|^2}
             \le C_\tau N^B e^{N(7/15+\tau)}.
 \tag{11}
\]
They hold for all real ordinary colors and on sufficiently small
fixed complex neighborhoods of complete color.
The same theorem gives, for \(|X-1|\le\delta<1\),
\[
 \frac{|p_j(X)|}{|P_j|}
 \le e^{N\Omega(\delta)},\qquad
 \Omega(\delta)=\log(1+\delta/2)
             +\frac{\delta}{2}\log(1+2/\delta).
 \tag{12}
\]
It follows directly from the full sums (1),(10) that
\[
 \sup_{|Y|\le1}|U_{0,N}(w,X)C_{1,N}(X,Y)|
 \le C_\tau N^B
 e^{N\{101/125+7/15+2\Omega(\delta)-\log(1-\delta)+\tau\}}.
 \tag{13}
\]
Since \(101/125+7/15=478/375<2383/1500\), a fixed
sufficiently small \(\delta\) and tolerance keep this prefix
below \(2383/1500\). This includes a fixed initial interval
\(0\le x\le\rho\), uniformly in the entire disk \(|Y|\le1\).
The Fourier weight \(d_N(Y)\) and the following conditional
kernel have not been included in (13); their marginal comparison
is still needed when using this prefix bound.

## 3. The incoming profile transport does not depend on \(q\)

Retain the cap profiles, conditional phase \(Q\), and fixed
conditional currents of
[the initial-interval proof, Sections 3--4](research_mixed_next_unselected_incoming_initial_interval.md).
The conditional real cuts are \(11/100,1/2\); their main and
auxiliary heights are the original \(h_s,-1/5,8\).
For a central private cap coordinate \(e\), or the extra real
profile \(e\in[.49,.5]\), the exact derivative is
\[
 \frac{d}{dx}\Re\{\Psi_0(e,x)+Q(v+i\eta;x,y)\}
 =\log\frac{|1-e^{-2\pi i(e+x)}|\,
                 |e^{-2\pi\eta}-e^{-2\pi i(x+v)}|}
                 {(2\sin\pi x)^2}
 >\log(3/2),
 \qquad \rho\le x\le1/10.
 \tag{14}
\]
As proved there, the first numerator modulus exceeds one,
the second exceeds \(3/5\), and the denominator is less than
\(2/5\). The formula is independent of \(y\). It therefore
transports every retained current to \(x=1/10\) also for
\(q\in[9/20,1/2]\). Both Fourier-weight alternatives and the
following kernel may be kept attached because they are
independent of \(x\).

This assertion compares individual current profiles. It does
not infer an estimate from the modulus of a signed endpoint
sum. Bounds for those individual endpoint profiles are required
before (14) can prove a complete-source bound.

## 4. The numerator at the first factorial zero

The finite conditional interpolation in the initial-interval
proof contains
\[
 e^{2\pi iNxs}
 \frac{\Pi_N(x+s)\Pi_N(y+s)}
      {\Pi_N(x)\Pi_N(y)\Pi_N(s)^3},\qquad
 \Pi_N(w)=e^{\pi iN(w-w^2)/2-\pi iw/2}G_N(Nw).
 \tag{15}
\]
At \(q=1/2\), the upper real cut \(\Re s=1/2\) reaches
\(\Re(y+s)=1\). One vertical current passes through \(y+s=1\)
itself. A relative nonzero factorial expansion cannot be used
there.

The already proved reflection estimate in
[the canonical row source, Section 3](research_repeated_two_block_canonical_row_source.md)
instead gives
\[
 |G_N(Nw)|\le C N^B
       e^{-N\Re J_{\mathrm{side}}(1-w)}
 \tag{16}
\]
on compact regions \(0<\Re w<2\) with bounded height, including
the entire first numerator-zero line. Its exact source identity is
\[
 G_N(Nw)=\frac{N}{G_N(Nv-1/2)},\qquad
                    v=1-w-\frac1{2N}.
 \tag{17}
\]
The reciprocal bound retains both reflected exponential terms.
The shift \(1/(2N)\) changes the primitive by
\(O(\log N/N)\), including at zero, accounting for the polynomial
factor in (16).

For \(0<\Re w\le1\), continuation from the real interval gives
\(J(w)=-J(1-w)\). Thus (16), with the exact chirp in (15),
has the original continuous upper rate \(\Re g(w)\).
The \(O(1/N)\) half-grid displacement of the cut has only
polynomial cost even if it falls just across that line.
All other arguments in (15) stay in their original regular
strips when \(x\in[\rho,.1]\), \(q\in[.45,.5]\) and
\(\Re s\in[.11,.5]\).

Accordingly the numerator zero is covered by an upper bound
for the original canonical source, with the original rate.
No physical row or contour current is removed at that zero,
and no relative expansion is asserted there. This permits the
endpoint-profile estimates required in Section 3 to include
\(q=1/2\), provided their phase inequalities are proved with
the same one-sided continuous branches.
