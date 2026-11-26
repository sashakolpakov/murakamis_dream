# A factorial interpolation on the entire outgoing interval

Research deduction, 7 November 2026. The reciprocal of the marked
factorial extends farther than the factorial itself. This gives one
holomorphic interpolation of every outgoing coefficient, including its
two endpoint values, on a rectangle of arbitrary finite height. The
continuation has zeros. They are kept explicitly below.

The resulting contour identity uses the original finite sum. It removes
the height restriction of the root-Pochhammer interpolation without
equating two functions merely because they agree on the lattice. It
does not yet estimate the full contour or prove a nonzero asymptotic.

## 1. Extending the reciprocal factorial

Fix an integer \(N\ge2\). Use the negative-root factorial from
[the outgoing factorial chart](research_mixed_fourier_right_cap_outer_contour.md):
\[
 \Pi_N(z)=G_N(Nz)
   \exp\!\left\{\frac{\pi i}{2}[N(z-z^2)-z]\right\}.
 \tag{1}
\]
The convergent Gamma product defining \(G_N\), including its
normalization, is proved in
[the factorial construction](exact_factorial_interpolation_and_complex_contours.md).
In particular \(\Pi_N\) is holomorphic and nonzero on
\(0<\Re z<1\), and on overlapping strips
\[
 \Pi_N(z+1/N)
       =(1-e^{-2\pi i(z+1/N)})\Pi_N(z).
 \tag{2}
\]

**Proposition 1.** The function \(1/\Pi_N\) has a unique
holomorphic extension \(E_N\) to \(\Re z<1\). On that half-plane
it is given by
\[
 E_N(z)=
 \frac{\displaystyle\prod_{k=1}^{m}
                    (1-e^{-2\pi i(z+k/N)})}
      {\Pi_N(z+m/N)},
 \qquad m\ge0,\quad 0<\Re(z+m/N)<1.
 \tag{3}
\]
Its only zeros are
\[
 z=-J/N,\qquad J=1,2,\ldots,
 \quad\text{of multiplicity }\lceil J/N\rceil.
 \tag{4}
\]
Also \(E_N(0)=1\).

*Proof.* For every \(z\) in the stated half-plane there is an
integer \(m\ge0\) satisfying (3). The same \(m\) works on a
neighborhood of that point. The expression is holomorphic there,
because the denominator belongs to the nonvanishing strip of
\(\Pi_N\).

Suppose two choices \(m<m'\) work. All intermediate arguments
\(z+k/N\), \(m\le k\le m'\), have real parts between zero
and one. Applying (2) through those arguments shows that the two
expressions (3) agree. These local expressions therefore define one
holomorphic function on \(\Re z<1\). It agrees with
\(1/\Pi_N\) on the original strip, so uniqueness follows from
the identity theorem.

Each numerator zero in (3) satisfies \(z+k/N\in\mathbb Z\).
Since \(k\le m\) and \(\Re(z+m/N)<1\), this integer is
nonpositive. Every zero is therefore of the form \(-J/N\),
with \(J\ge1\). Conversely, at that point choose \(m=J+1\),
so the denominator argument is \(1/N\). The vanishing factors
are exactly those \(1\le k\le J+1\) with \(k\equiv J\pmod N\).
There are \(\lfloor(J-1)/N\rfloor+1=\lceil J/N\rceil\)
of them, and each zero is simple in its factor. The denominator
does not vanish. Finally (3) at zero with \(m=1\), together
with \(\Pi_N(1/N)=1-e^{-2\pi i/N}\), gives \(E_N(0)=1\).
\(\square\)

The extension satisfies the identity
\[
 E_N(z)=(1-e^{-2\pi i(z+1/N)})E_N(z+1/N)
 \tag{5}
\]
whenever both arguments have real part below one. This is a
holomorphic identity even at its zeros. Dividing by the displayed
factor is unnecessary.

## 2. Every physical outgoing coefficient in the same chart

Keep the original output \(y=x_0\), and write
\[
 Y=e^{2\pi iy},\qquad r=e^{-2\pi i/N}.
 \tag{6}
\]
The inherited bounds are
\(.18299<\Re y<.18301\) and
\(.07871<\Im y<.07873\). Thus
\(0<\Re(1-y-1/N)<1\) for every \(N\ge2\).
Define
\[
 \widehat f_N(q;y)=
 \frac{e^{-\pi i(N-1)y}}N e^{2\pi iNyq}
               \Pi_N(1-y-1/N)E_N(q-y).
 \tag{7}
\]

**Proposition 2.** Formula (7) is holomorphic on
\(\Re q<1+\Re y\), with no restriction on \(\Im q\).
For every \(0\le l<N\),
\[
 \widehat f_N(l/N;y)=
 \frac{e^{-\pi i(N-1)y}}N
       Y^l\prod_{k=l+1}^{N-1}(1-Yr^k)=f_l(y).
 \tag{8}
\]
Its zeros are \(q=y-J/N\), \(J\ge1\), with the
multiplicities in (4).

*Proof.* Holomorphy and the zero statement follow from Proposition 1;
all other factors in (7) are nonzero. At \(q=l/N\), use
\(m=N-1-l\) in (3). Its denominator is precisely
\(\Pi_N(1-y-1/N)\), and its numerator is the product in (8).
This also proves the endpoint cases \(l=0\) and \(l=N-1\).
\(\square\)

On \(0<\Re(q-y)<1\), this is exactly the previously defined
factorial-suffix interpolation. Proposition 2 extends that same
function; it makes no assertion that it equals the independently
specified root-Pochhammer interpolation away from the lattice.

The exact recurrences, written without division, are
\[
 \begin{split}
 (1-Ye^{-2\pi i(q+1/N)})\widehat f_N(q+1/N;y)
                         &=Y\widehat f_N(q;y),\\
 (1-Y^Ne^{-2\pi iNq})\widehat f_N(q+1;y)
                         &=Y^N\widehat f_N(q;y).
 \end{split}
 \tag{9}
\]
The second follows by multiplying the first through one period;
both sides must lie in the domain of (7).

## 3. A full-period contour at arbitrary finite height

Use the exact low-index source from
[the source reduction](research_mixed_fourier_right_cap_low_index_source_reduction.md):
\[
 \begin{gathered}
 M_N=\lceil N/2\rceil-1,\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\quad X=e^{-2\pi ia},\\
 C_N^<(X,Z)=\sum_{j=0}^{M_N}
                   \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3}.
 \end{gathered}
 \tag{10}
\]
Every denominator is a nonzero finite factorial. Put
\[
 \widehat S_N(q)=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y).
 \tag{11}
\]
The first factor is an entire finite polynomial in \(e^{-2\pi iq}\).
If its coefficient vanishes, no division by that coefficient is made.
At a physical outgoing index, \(p_j(r^l)=0\) whenever
\(j+l\ge N\). Consequently
\[
 V_N^<=\sum_{l=0}^{N-1}\widehat S_N(l/N)
 =\sum_{j=0}^{M_N}\frac{X^{-j}p_j(X)}{P_j^3}
                  \sum_{l=0}^{N-j-1}p_j(r^l)f_l(y).
 \tag{12}
\]
This extension of the physical index range adds only zero terms.
The off-grid polynomial remains present on the entire contour.

Set \(\alpha_N=-1/(2N)\). The full rectangle with real
coordinates \([\alpha_N,\alpha_N+1]\) lies strictly inside
the domain of (11), for every finite choice of vertical heights.
Choose
\[
 h_-<h_0<0<h_+,
 \tag{13}
\]
where \(h_0\) is the original outgoing critical height. One
may, in particular, take \(h_-=-1/5\) and \(h_+=1/2\).
Define
\[
 \begin{split}
 \widehat Z_N&=N\int_{\alpha_N}^{\alpha_N+1}
                         \widehat S_N(q+ih_0)\,dq,\\
 \widehat L_N&=N\int_{\alpha_N}^{\alpha_N+1}
   \widehat S_N(q+ih_-)
       \frac{e^{-2\pi iN(q+ih_-)}}{1-e^{-2\pi iN(q+ih_-)}}\,dq,\\
 \widehat U_N&=N\int_{\alpha_N}^{\alpha_N+1}
   \widehat S_N(q+ih_+)
       \frac{e^{2\pi iN(q+ih_+)}}{1-e^{2\pi iN(q+ih_+)}}\,dq,\\
 \widehat B_N&=iN\int_{h_-}^{h_+}
   \left(\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<h_0\}}\right)
   [\widehat S_N(\alpha_N+1+iv)
                      -\widehat S_N(\alpha_N+iv)]\,dv.
 \end{split}
 \tag{14}
\]

**Theorem 3.** At every integer level of either parity,
\[
             V_N^<=\widehat Z_N+\widehat L_N
                                  +\widehat U_N+\widehat B_N.
 \tag{15}
\]
All internal cuts cancel if the interval is subdivided while using
this same interpolation and the same heights.

*Proof.* Apply the proved
[one-index residue identity](research_exact_vertical_current_regrouping.md)
to the holomorphic function (11) on the indicated rectangle.
It contains exactly the lattice points \(l/N\), \(0\le l<N\).
Its residue sum is (12), and its four integrals are (14).
At an internal cut the right and left vertical integrals have
opposite orientations and identical integrands. The horizontal
pieces concatenate. This proves both assertions. \(\square\)

The zeros crossed when raising the contour cause no poles in this
argument. In the full-period rectangle they have the form
\(y-J/N\), with \(1\le J<N\), and are simple. They must
still be retained when estimating the modulus of (11).

## 4. The exact endpoint relation and the estimates still needed

The polynomial in (11) has period one. At
\(q=\alpha_N+iv\), (9) therefore gives the holomorphic identity
\[
 (1+Y^Ne^{2\pi Nv})\widehat S_N(\alpha_N+1+iv)
                      =Y^N\widehat S_N(\alpha_N+iv).
 \tag{16}
\]
Below the root-Pochhammer height restriction, this can be written
as the quotient used in
[the earlier full-period regrouping](research_mixed_fourier_right_cap_low_index_outgoing_regrouping.md).
On a taller contour the denominator in that quotient can be small.
The original functions in (14) remain holomorphic, and any apparent
pole of the quotient is canceled by a zero of its numerator.
Equation (16), or the undivided difference in (14), retains that
cancellation. No lower bound for the quotient's denominator is
assumed.

On the old central strip the previous factorial expansion and
its phase estimates apply to (7) unchanged. Outside that strip,
the finite product in (3) is part of the interpolation. In
particular its zeros cannot be suppressed by continuing a
nonvanishing leading symbol through them.

Thus (15) supplies one exact contour over the whole outgoing
period at the tall heights already used in the central analysis.
The complete upper and lower Fourier corrections, the main path
outside the central interval, and the true boundary difference
still need bounds. The coefficient of the vertical integral is
of order one between \(h_0\) and zero; that segment has no
automatic Fourier decay. Neither the continuation nor its exact
recurrences prove a whole-source lower bound.
